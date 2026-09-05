import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="A Surprise for Ricky ❤️",
    page_icon="💗",
    layout="wide"
)

# -----------------------------
# LOAD FILES FROM assets FOLDER
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR_CANDIDATES = (
    BASE_DIR / "assests",
    BASE_DIR / "assets",
    Path.cwd() / "assests",
    Path.cwd() / "assets",
)
ASSETS_DIR = next(
    (directory for directory in ASSET_DIR_CANDIDATES if directory.is_dir()),
    BASE_DIR / "assests",
)
THEME_CSS = (BASE_DIR / "theme.css").read_text(encoding="utf-8")
ASSET_BASE_URL = "https://raw.githubusercontent.com/chinnu1729/BR/main/assests"


def get_asset_url(filename):
    path = ASSETS_DIR / filename

    if not path.is_file():
        return ""

    return f"{ASSET_BASE_URL}/{filename}"


photo1 = get_asset_url("photo1.jpeg")
photo2 = get_asset_url("photo2.jpeg")
photo3 = get_asset_url("photo3.jpeg")
song = get_asset_url("song.mp3")
couple_image = get_asset_url("original-9b40aa4942f5c0336b8132f60e348015.webp")
final_video = get_asset_url("large-thumbnail20251111-2516313-k43kam.mp4")
page2_video = get_asset_url("2.mp4")
page3_video = get_asset_url("3.mp4")
page4_video = get_asset_url("5.mp4")
page5_video = get_asset_url("4.mp4")
page_before_last_video = get_asset_url("05.mp4")


missing_photos = [
    filename
    for filename, data in {
        "photo1.jpeg": photo1,
        "photo2.jpeg": photo2,
        "photo3.jpeg": photo3,
    }.items()
    if not data
]

if missing_photos:
    st.warning(
        "Missing photos: "
        + ", ".join(missing_photos)
        + f". Resolved asset folder: {ASSETS_DIR}"
    )


# -----------------------------
# HTML WEBSITE
# -----------------------------
html_code = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Nunito:wght@400;600;700;800&display=swap');

:root {
    --plum: #321d48;
    --deep-plum: #20122f;
    --peach: #ffb486;
    --coral: #ed6f86;
    --lilac: #c5a8e8;
    --cream: #fff0db;
}

* { box-sizing: border-box; }

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
}

body {
    font-family: "Nunito", "Trebuchet MS", sans-serif;
    overflow: hidden;
    background: var(--deep-plum);
}

.page {
    width: 100%;
    height: 850px;
    display: none;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    text-align: center;
    padding: 25px;
    position: relative;
    overflow: hidden;
}

.page.active {
    display: flex;
    animation: pageReveal .8s cubic-bezier(.2,.8,.2,1) both;
}

@keyframes pageReveal {
    from { opacity: 0; transform: scale(1.06); }
    to { opacity: 1; transform: scale(1); }
}

.page::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,.16), transparent 18%),
        radial-gradient(circle at 80% 25%, rgba(255,255,255,.12), transparent 20%),
        radial-gradient(circle at 50% 85%, rgba(255,130,190,.18), transparent 25%);
    pointer-events: none;
}

.page::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image: url("__COUPLE_IMAGE__");
    background-repeat: no-repeat;
    background-position: right 7% bottom 4%;
    background-size: min(500px, 48vw) auto;
    opacity: .86;
    filter: saturate(1.12) drop-shadow(0 18px 18px rgba(35, 16, 47, .25));
    pointer-events: none;
    z-index: 1;
}

#page1 {
    background: url("__COUPLE_IMAGE__") center / cover no-repeat;
}

#page1::after {
    display: none;
}

#page2::after {
    background-position: left 5% bottom 2%;
    background-size: min(440px, 44vw) auto;
}

#page3::after {
    background-position: right 2% top 8%;
    background-size: min(390px, 38vw) auto;
}

#page4::after {
    background-position: left 3% bottom 4%;
    background-size: min(360px, 36vw) auto;
}

#page5::after {
    background-position: right 4% top 5%;
    background-size: min(420px, 42vw) auto;
}

#page6::after {
    background-position: center bottom 0;
    background-size: min(560px, 54vw) auto;
}

.content {
    position: relative;
    z-index: 5;
    width: 100%;
    max-width: 900px;
    animation: contentEnter .7s ease both;
}

@keyframes contentEnter {
    from { opacity: 0; transform: translateY(18px) scale(.98); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}

.pink {
    color: #ffb6d8;
}

.eyebrow {
    font-size: 15px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #ffe9f4;
    margin-bottom: 12px;
}

.title {
    font-family: "Baloo 2", "Trebuchet MS", sans-serif;
    font-size: 48px;
    font-weight: 800;
    line-height: 1.2;
    color: var(--cream);
    text-shadow: 0 4px 0 rgba(90, 38, 79, .55), 0 10px 22px rgba(0,0,0,.22);
}

.subtitle {
    font-size: 20px;
    color: #ffeaf5;
    line-height: 1.6;
    margin: 12px auto;
    max-width: 650px;
}

button {
    border: none;
    background: linear-gradient(145deg, var(--peach), var(--coral));
    color: #43203f;
    padding: 14px 30px;
    border-radius: 18px;
    font-size: 18px;
    font-family: "Baloo 2", sans-serif;
    font-weight: 700;
    cursor: pointer;
    margin-top: 22px;
    box-shadow: inset 0 -4px 0 rgba(165, 58, 93, .28), 0 10px 0 rgba(36, 17, 54, .3), 0 16px 28px rgba(15, 7, 25, .22);
}

button:active {
    transform: scale(.95);
}

/* PAGE 1 */
#page1 {
    background: url("__COUPLE_IMAGE__") center / cover no-repeat;
}

.heart {
    font-size: 110px;
    cursor: pointer;
    animation: heartbeat 1.3s infinite;
    position: relative;
    z-index: 5;
}

.heart.clicked {
    animation: heartLaunch .55s cubic-bezier(.2,.8,.2,1) both;
}

@keyframes heartLaunch {
    50% { transform: scale(1.5) rotate(8deg); filter: brightness(1.35); }
    100% { transform: scale(.2) rotate(-16deg); opacity: 0; }
}

@keyframes heartbeat {
    0%,100% { transform: scale(1); }
    50% { transform: scale(1.14); }
}

.tap {
    color: #fff;
    margin-top: 12px;
    font-size: 17px;
}

/* PAGE 2 */
#page2 {
    background: radial-gradient(circle at 50% 15%, #ffd0a8 0%, #bd80bd 38%, #39204f 100%);
}

.cake {
    font-size: 125px;
    animation: float 2s ease-in-out infinite;
}

@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-14px); }
}

/* PAGE 3 */
#page3 {
    background: radial-gradient(circle at 20% 10%, #8f66ae 0%, #4d285e 48%, #21132f 100%);
}

.balloon-area {
    width: 100%;
    max-width: 600px;
    height: 260px;
    position: relative;
    margin: 5px auto;
}

.balloon {
    position: absolute;
    font-size: 70px;
    animation: balloonFloat 3s ease-in-out infinite;
}

.balloon1 { left: 8%; top: 100px; }
.balloon2 { left: 32%; top: 25px; animation-delay: .5s; }
.balloon3 { right: 30%; top: 115px; animation-delay: 1s; }
.balloon4 { right: 7%; top: 45px; animation-delay: 1.5s; }

@keyframes balloonFloat {
    0%,100% { transform: translateY(0) rotate(-3deg); }
    50% { transform: translateY(-22px) rotate(3deg); }
}

.note {
    background: linear-gradient(145deg, rgba(255, 205, 177, .3), rgba(193, 157, 225, .18));
    border: 1px solid rgba(255, 226, 213, .35);
    padding: 12px 18px;
    margin: 8px auto;
    border-radius: 18px;
    color: white;
    max-width: 480px;
    box-shadow: inset 0 2px 0 rgba(255,255,255,.25), 0 10px 22px rgba(17, 8, 31, .18);
}

/* PAGE 4 */
#page4 {
    background: radial-gradient(circle at 50% 0%, #bd7ba0 0%, #5d315f 50%, #21132f 100%);
}

.photos {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
    margin-top: 20px;
}

.card {
    width: 220px;
    background: linear-gradient(145deg, #ffd9bf, #e8b5ce);
    padding: 9px;
    border-radius: 8px;
    box-shadow: inset 0 2px 0 rgba(255,255,255,.5), 0 14px 0 rgba(50, 24, 62, .35), 0 22px 30px rgba(0,0,0,.3);
}

.card:nth-child(1) { transform: rotate(-3deg); }
.card:nth-child(2) { transform: rotate(2deg); }
.card:nth-child(3) { transform: rotate(-1deg); }

.card img {
    width: 100%;
    height: 245px;
    object-fit: cover;
    display: block;
    border-radius: 5px;
}

.caption {
    color: #54264e;
    font-family: "Nunito", sans-serif;
    font-weight: bold;
    font-size: 14px;
    padding: 9px 4px 5px;
}

.missing {
    height: 245px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #efd5e2;
    color: #7d4562;
    font-family: Arial, sans-serif;
}

/* PAGE 5 */
#page5 {
    background: radial-gradient(circle at 50% 5%, #ce87a7 0%, #64315f 48%, #21132f 100%);
}

.envelope {
    font-size: 120px;
    cursor: pointer;
    animation: envelopeFloat 1.5s infinite;
}

@keyframes envelopeFloat {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.letter {
    display: none;
    width: 92%;
    max-width: 620px;
    background: linear-gradient(145deg, #ffe1c6, #f1bfd0);
    color: #5e3b4b;
    padding: 27px;
    border-radius: 22px;
    box-shadow: inset 0 2px 0 rgba(255,255,255,.55), 0 15px 0 rgba(48, 22, 60, .28), 0 25px 45px rgba(0,0,0,.4);
    font-family: "Nunito", sans-serif;
    font-size: 17px;
    line-height: 1.7;
    position: relative;
    z-index: 10;
}

.letter h2 {
    color: #d34e83;
    font-family: "Baloo 2", sans-serif;
}

/* PAGE 6 */
#page6 {
    background: radial-gradient(circle at 50% 5%, #ffc39f 0%, #9c5d99 44%, #321634 100%);
}

.final-heart {
    font-size: 110px;
    animation: heartbeat 1.4s infinite;
}

.final-title {
    font-family: "Baloo 2", sans-serif;
    font-size: 48px;
    font-weight: 800;
    color: var(--cream);
    text-shadow: 0 4px 0 rgba(90, 38, 79, .55), 0 10px 25px rgba(0,0,0,.3);
}

.final-text {
    color: white;
    font-size: 20px;
    margin-top: 12px;
}

/* STARS */
.star {
    position: absolute;
    color: white;
    opacity: .7;
    animation: twinkle 2s infinite alternate;
    z-index: 1;
}

@keyframes twinkle {
    from { opacity: .2; transform: scale(.8); }
    to { opacity: 1; transform: scale(1.2); }
}

/* MOBILE */
@media (max-width: 600px) {
    .page { height: 850px; padding: 18px 12px; }
    .page::after {
        background-position: right -8% bottom 2%;
        background-size: 300px auto;
        opacity: .72;
    }
    #page1 { background-position: 58% center; }
    #page1::after { display: none; }
    .title { font-size: 30px; }
    .subtitle { font-size: 17px; }
    .heart { font-size: 90px; }
    .cake { font-size: 95px; }
    .balloon-area { height: 230px; }
    .balloon { font-size: 52px; }
    .card { width: 145px; }
    .card img, .missing { height: 180px; }
    .caption { font-size: 11px; }
    .envelope { font-size: 95px; }
    .letter { font-size: 15px; padding: 20px; }
    .final-title { font-size: 30px; }
}
</style>
<style>
__THEME_CSS__
</style>
</head>

<body>

<!-- PAGE 1 -->
<div class="page active" id="page1">
    <div class="content">
        <div class="eyebrow">a little surprise for you 💗</div>
        <div class="title">A Surprise for Ricky</div>
        <div class="subtitle">I made something special for you...</div>
        <div class="heart" id="start">💝</div>
        <div class="tap">Tap the heart ✨</div>
    </div>
</div>

<!-- PAGE 2 -->
<div class="page" id="page2">
    <video class="page-video" autoplay muted loop playsinline>
        <source src="__PAGE2_VIDEO__" type="video/mp4">
    </video>
    <div class="content">
        <div class="eyebrow">it's your special day 🎂</div>
        <div class="cake">🎂</div>
        <div class="title">HAPPY BIRTHDAY<br>RICKY ❤️</div>
        <div class="subtitle">
            Wishing you happiness, success and lots of beautiful moments ✨
        </div>
        <button id="next2">Continue 💗</button>
    </div>
</div>

<!-- PAGE 3 -->
<div class="page" id="page3">
    <video class="page-video" autoplay muted loop playsinline>
        <source src="__PAGE3_VIDEO__" type="video/mp4">
    </video>
    <div class="content">
        <div class="eyebrow">a few little things 🎈</div>
        <div class="title">For You 💕</div>

        <div class="balloon-area">
            <div class="balloon balloon1">🎈</div>
            <div class="balloon balloon2">🎈</div>
            <div class="balloon balloon3">🎈</div>
            <div class="balloon balloon4">🎈</div>
        </div>

        <div class="note">Your smile is one of the sweetest things ❤️</div>
        <div class="note">You deserve lots of happiness ✨</div>
        <div class="note">Keep smiling and keep being amazing 💗</div>

        <button id="next3">See Our Memories 📸</button>
    </div>
</div>

<!-- PAGE 4 -->
<div class="page" id="page4">
    <video class="page-video" autoplay muted loop playsinline>
        <source src="__FINAL_VIDEO__" type="video/mp4">
    </video>
    <div class="content">
        <div class="eyebrow">a walk down memory lane ✨</div>
        <div class="title">Beautiful Memories 💕</div>

        <div class="photos">

            <div class="card">
                __PHOTO1__
                <div class="caption">A little piece of happiness ❤️</div>
            </div>

            <div class="card">
                __PHOTO2__
                <div class="caption">My favourite memory 💗</div>
            </div>

            <div class="card">
                __PHOTO3__
                <div class="caption">One more beautiful moment ✨</div>
            </div>

        </div>

        <button id="next4">One More Thing 💌</button>
    </div>
</div>

<!-- PAGE 5 -->
<div class="page" id="page5">
    <video class="page-video" autoplay muted loop playsinline>
        <source src="__PAGE_BEFORE_LAST_VIDEO__" type="video/mp4">
    </video>
    <div class="content">
        <div class="eyebrow">one last thing...</div>
        <div class="title">I Have Something For You 💌</div>

        <div class="envelope" id="envelope">💌</div>
        <div class="tap" id="envelopeText">Tap the envelope</div>

        <div class="letter" id="letter">
            <h2>Happy Birthday, Ricky ❤️</h2>

            <p>
                I hope this new year of your life brings you
                lots of happiness, beautiful memories and success. ✨
            </p>

            <p>
                Keep smiling, keep dreaming and keep being
                the wonderful person you are. 💗
            </p>

            <p>
                May every little wish of yours find its way to you. 🎂✨
            </p>

            <p>
                Wishing you the happiest birthday! ❤️
            </p>

            <button id="finalButton">Final Surprise 🎉</button>
        </div>
    </div>
</div>

<!-- PAGE 6 -->
<div class="page" id="page6">
    <video class="page-video" autoplay muted loop playsinline>
        <source src="__PAGE5_VIDEO__" type="video/mp4">
    </video>
    <div class="content">
        <div class="final-heart">❤️</div>
        <div class="final-title">HAPPY BIRTHDAY RICKY! 🎉</div>
        <div class="final-text">
            Hope your day is as special as you are 💗✨
        </div>
        <div style="font-size:60px;margin-top:25px;">
            🎂 🎈 🎁 💕
        </div>
    </div>
</div>

<audio id="music" loop>
    <source src="__SONG__" type="audio/mpeg">
</audio>

<script>

function showPage(number) {
    document.querySelectorAll(".page").forEach(function(page) {
        page.classList.remove("active");
    });

    document.getElementById("page" + number).classList.add("active");
}

var music = document.getElementById("music");

document.getElementById("start").addEventListener("click", function() {
    document.getElementById("start").classList.add("clicked");
    music.play().catch(function() {});
    setTimeout(function() {
        showPage(2);
    }, 500);
});

document.getElementById("next2").addEventListener("click", function() {
    showPage(3);
});

document.getElementById("next3").addEventListener("click", function() {
    showPage(4);
});

document.getElementById("next4").addEventListener("click", function() {
    showPage(5);
});

document.getElementById("envelope").addEventListener("click", function() {
    document.getElementById("envelope").style.display = "none";
    document.getElementById("envelopeText").style.display = "none";
    document.getElementById("letter").style.display = "block";
});

document.getElementById("finalButton").addEventListener("click", function() {
    showPage(6);
    createConfetti();
});

function createConfetti() {

    var emojis = [
        "❤️", "💗", "💕", "🎉",
        "✨", "🎈", "🎁", "🌸"
    ];

    for (var i = 0; i < 90; i++) {

        var item = document.createElement("div");

        item.innerHTML =
            emojis[Math.floor(Math.random() * emojis.length)];

        item.style.position = "fixed";
        item.style.left = Math.random() * 100 + "%";
        item.style.top = "-40px";
        item.style.fontSize =
            (15 + Math.random() * 25) + "px";
        item.style.zIndex = "99999";

        document.body.appendChild(item);

        var duration =
            2200 + Math.random() * 2800;

        item.animate(
            [
                {
                    transform:
                        "translateY(0) rotate(0deg)"
                },
                {
                    transform:
                        "translateY(100vh) rotate(720deg)"
                }
            ],
            {
                duration: duration,
                easing: "linear"
            }
        );

        setTimeout(
            function(el) {
                return function() {
                    el.remove();
                };
            }(item),
            duration
        );
    }
}

function createStars() {

    var pages =
        document.querySelectorAll(".page");

    pages.forEach(function(page) {

        for (var i = 0; i < 22; i++) {

            var star =
                document.createElement("div");

            star.className = "star";
            star.innerHTML = "✦";

            star.style.left =
                Math.random() * 100 + "%";

            star.style.top =
                Math.random() * 100 + "%";

            star.style.fontSize =
                (8 + Math.random() * 12) + "px";

            star.style.animationDelay =
                Math.random() * 2 + "s";

            page.appendChild(star);
        }
    });
}

createStars();

</script>

</body>
</html>
"""


# -----------------------------
# PUT PHOTOS INTO HTML
# -----------------------------
def make_image_tag(data, alt):

    if data:
        return f'<img src="{data}" alt="{alt}">'

    return '<div class="missing">Photo not found 💔</div>'


html_code = html_code.replace(
    "__PHOTO1__",
    make_image_tag(photo1, "Memory 1")
)

html_code = html_code.replace(
    "__PHOTO2__",
    make_image_tag(photo2, "Memory 2")
)

html_code = html_code.replace(
    "__PHOTO3__",
    make_image_tag(photo3, "Memory 3")
)

html_code = html_code.replace(
    "__SONG__",
    song
)

html_code = html_code.replace(
    "__THEME_CSS__",
    THEME_CSS
)

html_code = html_code.replace(
    "__COUPLE_IMAGE__",
    couple_image
)

html_code = html_code.replace(
    "__FINAL_VIDEO__",
    final_video
)

html_code = html_code.replace(
    "__PAGE2_VIDEO__",
    page2_video
)

html_code = html_code.replace(
    "__PAGE3_VIDEO__",
    page3_video
)

html_code = html_code.replace(
    "__PAGE4_VIDEO__",
    page4_video
)

html_code = html_code.replace(
    "__PAGE5_VIDEO__",
    page5_video
)

html_code = html_code.replace(
    "__PAGE_BEFORE_LAST_VIDEO__",
    page_before_last_video
)

# -----------------------------
# SHOW WEBSITE
# -----------------------------
components.html(
    html_code,
    height=850,
    scrolling=False
)