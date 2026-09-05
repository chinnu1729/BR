"""Small dependency-free backend for the birthday surprise app."""

from __future__ import annotations

import json
import mimetypes
import threading
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assests"
if not ASSETS_DIR.is_dir():
    ASSETS_DIR = BASE_DIR / "assets"

EVENTS: list[dict[str, str]] = []
EVENTS_LOCK = threading.Lock()
ALLOWED_ASSETS = {"photo1.jpeg", "photo2.jpeg", "photo3.jpeg", "song.mp3"}

SURPRISE = {
    "recipient": "Ricky",
    "title": "A Surprise for Ricky",
    "messages": [
        "Your smile is one of the sweetest things.",
        "You deserve lots of happiness.",
        "Keep smiling and keep being amazing.",
    ],
    "memories": [
        {"file": "photo1.jpeg", "caption": "A little piece of happiness"},
        {"file": "photo2.jpeg", "caption": "My favourite memory"},
        {"file": "photo3.jpeg", "caption": "One more beautiful moment"},
    ],
}


class BackendHandler(BaseHTTPRequestHandler):
    server_version = "BirthdaySurprise/1.0"

    def do_GET(self) -> None:
        route = urlparse(self.path).path
        if route == "/api/health":
            self.send_json({"status": "ok", "service": "birthday-surprise"})
            return
        if route == "/api/surprise":
            payload = dict(SURPRISE)
            payload["memories"] = [
                {**memory, "url": f"/assets/{memory['file']}"}
                for memory in SURPRISE["memories"]
            ]
            payload["musicUrl"] = "/assets/song.mp3"
            self.send_json(payload)
            return
        if route.startswith("/assets/"):
            self.send_asset(unquote(route.removeprefix("/assets/")))
            return
        self.send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/events":
            self.send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
            return

        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size > 4096:
                raise ValueError("request too large")
            body = json.loads(self.rfile.read(size) or b"{}")
            event = str(body.get("event", "")).strip()
            if not event or len(event) > 80:
                raise ValueError("event must be a short non-empty string")
        except (ValueError, json.JSONDecodeError):
            self.send_json({"error": "Invalid event payload"}, HTTPStatus.BAD_REQUEST)
            return

        record = {
            "event": event,
            "at": datetime.now(timezone.utc).isoformat(),
        }
        with EVENTS_LOCK:
            EVENTS.append(record)
        self.send_json({"received": True, "event": record}, HTTPStatus.CREATED)

    def send_asset(self, filename: str) -> None:
        if filename not in ALLOWED_ASSETS:
            self.send_json({"error": "Asset not found"}, HTTPStatus.NOT_FOUND)
            return
        asset = ASSETS_DIR / filename
        if not asset.is_file():
            self.send_json({"error": "Asset not found"}, HTTPStatus.NOT_FOUND)
            return
        content_type = mimetypes.guess_type(asset.name)[0] or "application/octet-stream"
        data = asset.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "public, max-age=3600")
        self.end_headers()
        self.wfile.write(data)

    def send_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")


def create_server(host: str = "127.0.0.1", port: int = 8000) -> ThreadingHTTPServer:
    return ThreadingHTTPServer((host, port), BackendHandler)


if __name__ == "__main__":
    server = create_server()
    print("Birthday surprise backend running at http://127.0.0.1:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping backend...")
    finally:
        server.server_close()
