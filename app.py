import os
from flask import Flask, render_template_string, url_for  # Added url_for here

app = Flask(__name__)


@app.route("/")
def birthday_fun():
    # Enna prechana na, template string ulla Flask context variables direct ah pass pannanum
    # Adhuku Jinja syntax (double curly braces) use panni 'url_for' call pannanum.
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Surprise Mapla!</title>
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Poppins:wght@400;700;800&family=Bungee&display=swap" rel="stylesheet">
        <style>
            :root {
                --bg-color: #FFFFFF;
                --text-dark: #2d3436;
                --text-light: #636e72;
                
                --primary-pink: #ff6b6b;
                --primary-purple: #a55eea;
                --primary-blue: #4bcffa;
                --neon-yellow: #feca57;
                
                --panel-bg: rgba(255, 255, 255, 0.9);
                --shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            body { 
                background-color: var(--bg-color); 
                color: var(--text-dark); 
                font-family: 'Poppins', sans-serif; 
                text-align: center; 
                margin: 0; 
                padding: 0;
                overflow-x: hidden;
            }

            .screen {
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
                min-height: 100vh;
                width: 100vw;
                position: relative;
                padding: 30px 20px;
                box-sizing: border-box;
            }
            
            #countdown-screen {
                justify-content: center;
                background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            }

            #countdown {
                font-size: 15rem;
                font-family: 'Bungee', sans-serif;
                color: var(--text-dark);
                text-shadow: 
                    4px 4px 0px var(--primary-pink),
                    8px 8px 0px var(--primary-purple),
                    12px 12px 20px rgba(0,0,0,0.2);
                margin: 0;
                animation: attractiveNums 1s infinite;
            }
            
            @keyframes attractiveNums {
                0% { transform: scale(1); text-shadow: 4px 4px 0px var(--primary-pink), 8px 8px 0px var(--primary-purple); }
                50% { transform: scale(1.1); text-shadow: 4px 4px 0px var(--primary-blue), 8px 8px 0px var(--neon-yellow); color: #000; }
                100% { transform: scale(1); text-shadow: 4px 4px 0px var(--primary-pink), 8px 8px 0px var(--primary-purple); }
            }

            @media (max-width: 600px) {
                #countdown { font-size: 8rem; }
            }
            
            #main-content { display: none; }
            
            .banner-21 {
                background: var(--panel-bg);
                border: 3px solid var(--primary-purple);
                padding: 12px 30px;
                border-radius: 50px;
                box-shadow: var(--shadow);
                margin-bottom: 25px; 
                max-width: 90%;
            }
            .title-21 {
                font-size: 1.5rem;
                font-weight: 800;
                color: var(--text-dark);
                letter-spacing: 1px;
                margin: 0;
            }
            @media (max-width: 600px) {
                .title-21 { font-size: 1.1rem; }
            }
            
            .arc-container {
                width: 100%;
                max-width: 650px;
                height: 180px; 
                margin: 10px auto 0 auto; 
                display: block;
                overflow: visible;
            }
            
            .arc-text {
                font-family: 'Bungee', cursive;
                letter-spacing: 2px;
            }
            
            .word-happy {
                font-size: 38px;
                fill: var(--primary-pink);
                filter: drop-shadow(2px 2px 4px rgba(255, 107, 107, 0.5));
            }
            .word-birthday {
                font-size: 36px;
                fill: var(--primary-purple);
                filter: drop-shadow(2px 2px 4px rgba(165, 94, 234, 0.5));
            }
            .word-ngo {
                font-size: 42px;
                fill: var(--primary-blue);
                filter: drop-shadow(2px 2px 5px rgba(75, 207, 250, 0.5));
            }

            @media (max-width: 520px) {
                .word-happy { font-size: 24px; }
                .word-birthday { font-size: 22px; }
                .word-ngo { font-size: 26px; }
                .arc-container { height: 110px; margin-top: 10px; }
            }

            .profile-pic-container {
                margin-top: -65px; 
                margin-bottom: 30px;
                width: 195px;
                height: 195px;
                border-radius: 50%;
                overflow: hidden;
                border: 8px solid #000000;
                box-shadow: var(--shadow);
                position: relative;
                z-index: 10;
                background-color: #eee;
            }

            .profile-pic-container img {
                width: 100%;
                height: 100%;
                object-fit: cover;
                display: block;
            }

            @media (max-width: 520px) {
                .profile-pic-container {
                    width: 140px;
                    height: 140px;
                    margin-top: -40px;
                }
            }
            
            .scroll-down {
                font-size: 1.1rem;
                color: var(--text-light);
                font-weight: 700;
                margin-top: auto; 
                padding-top: 20px;
                letter-spacing: 1px;
            }
            .arrow { font-size: 2rem; color: var(--primary-purple); margin-top: 5px; animation: bounce 2s infinite; }
            
            .message-section, #gallery-section {
                min-height: 100vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding: 40px 20px;
                box-sizing: border-box;
                background-color: #fcfcfc;
                border-top: 1px solid #eee;
            }
            
            .msg-box, .gallery-box {
                background: #FFFFFF;
                border: 1px solid #eee;
                padding: 40px 30px;
                border-radius: 30px;
                max-width: 700px;
                width: 100%;
                box-shadow: var(--shadow);
                box-sizing: border-box;
            }
            
            .msg-box b { 
                font-size: 2.2rem; 
                color: var(--primary-pink); 
                display: block; 
                margin-bottom: 20px;
                font-family: 'Montserrat', sans-serif;
                font-weight: 900;
            }
            
            .msg-box p.intro-p { font-size: 1.15rem; line-height: 1.8; color: var(--text-dark); margin: 15px 0; }
            
            .poem-wrapper {
                margin-top: 35px;
                border-top: 2px solid #eee;
                padding-top: 25px;
            }
            .quote-title { 
                font-weight: 800; 
                color: var(--primary-purple);
                letter-spacing: 2px; 
                font-size: 1.8rem;
                font-family: 'Poppins', sans-serif;
                margin-bottom: 25px;
            }
            
            #poem-content {
                display: none;
                background: #fdfafb;
                border: 2px solid rgba(255, 107, 107, 0.15);
                border-radius: 20px;
                padding: 25px 20px;
                margin: 20px 0;
                animation: slideDown 0.6s ease-out forwards;
                box-shadow: inset 0 2px 8px rgba(0,0,0,0.02);
            }
            
            .quote-line { 
                font-style: italic; 
                color: #212529; 
                font-size: 1.25rem; 
                margin: 20px 0;
                line-height: 1.7;
                border-left: 4px solid var(--primary-pink);
                padding-left: 15px;
                text-align: left;
                font-weight: 500;
            }
            
            .action-btn {
                background: linear-gradient(45deg, var(--primary-pink), #ff8787);
                color: white; border: none; padding: 18px 40px;
                border-radius: 50px; font-size: 1.1rem; font-weight: 800;
                cursor: pointer; margin: 15px 0; transition: 0.3s;
                box-shadow: 0 5px 15px rgba(255, 107, 107, 0.3);
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .action-btn:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(255, 107, 107, 0.4); }
            
            #post-blast-box {
                display: none;
                margin-top: 40px;
                padding-top: 30px;
                border-top: 2px dashed #eee;
                animation: fadeIn 0.8s ease-in forwards;
            }
            .surprise-text {
                font-size: 1.2rem;
                font-weight: 600;
                color: var(--text-dark);
                line-height: 1.8;
                margin-bottom: 30px;
            }
            
            .aurahvn-btn {
                background: linear-gradient(45deg, var(--primary-purple), #c394f1);
                color: white; border: none; padding: 20px 50px;
                border-radius: 50px; font-size: 1.4rem; font-weight: 800;
                cursor: pointer; transition: 0.3s;
                box-shadow: 0 5px 20px rgba(165, 94, 234, 0.3);
                letter-spacing: 2px;
            }
            .aurahvn-btn:hover { 
                transform: translateY(-3px); 
                box-shadow: 0 10px 30px rgba(165, 94, 234, 0.5);
            }

            #gallery-section {
                display: none; 
                background-color: var(--bg-color);
                padding-top: 60px;
                padding-bottom: 80px;
            }
            
            .gallery-box {
                background: #FFFFFF;
                border: 1px solid #eee;
                padding: 40px 30px;
                border-radius: 30px;
                max-width: 700px;
                width: 100%;
                box-shadow: var(--shadow);
                box-sizing: border-box;
            }

            .gallery-question {
                font-size: 2.2rem;
                font-weight: 800;
                color: var(--text-dark);
                margin-bottom: 40px;
                font-family: 'Montserrat', sans-serif;
            }
            
            .option-btn-container, .device-btn-container {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-bottom: 35px;
            }
            
            .opt-btn, .dev-btn {
                background: white;
                color: var(--primary-purple);
                border: 2px solid var(--primary-purple);
                padding: 15px 30px;
                border-radius: 50px;
                font-size: 1.1rem;
                font-weight: 700;
                cursor: pointer;
                transition: 0.3s;
                min-width: 160px;
            }
            .opt-btn:hover, .opt-btn.active {
                background: var(--primary-purple);
                color: white;
                box-shadow: 0 5px 15px rgba(165, 94, 234, 0.3);
            }

            .dev-btn {
                color: var(--primary-blue);
                border: 2px solid var(--primary-blue);
            }
            .dev-btn:hover, .dev-btn.active {
                background: var(--primary-blue);
                color: white;
                box-shadow: 0 5px 15px rgba(75, 207, 250, 0.3);
            }
            
            .display-area {
                margin-top: 30px;
                min-height: 400px;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            
            .image-display-wrapper {
                width: 100%;
                max-width: 500px;
                border-radius: 20px;
                overflow: hidden;
                box-shadow: var(--shadow);
                border: 5px solid white;
                margin-bottom: 25px;
                display: none; 
                background-color: #eee; 
            }
            
            .image-display-wrapper img {
                width: 100%;
                height: auto;
                display: block;
            }
            
            .img-placeholder {
                width: 100%;
                height: 300px;
                display: flex;
                justify-content: center;
                align-items: center;
                color: #aaa;
                font-weight: bold;
                background-color: #fafafa;
            }
            
            #final-surprise-area {
                display: none; 
                margin-top: 50px;
                padding-top: 40px;
                border-top: 3px dashed #eee;
                animation: slideDown 0.8s ease-out forwards;
                width: 100%;
                align-items: center;
                flex-direction: column;
            }
            
            .core-justification-block {
                width: 100%;
                max-width: 620px;
                background: #f9f9f9;
                border-left: 5px solid var(--primary-purple);
                padding: 20px 25px;
                margin-bottom: 35px;
                text-align: left;
                border-radius: 0 15px 15px 0;
                box-shadow: 0 4px 15px rgba(0,0,0,0.02);
                box-sizing: border-box;
            }
            
            .core-line {
                font-size: 1.1rem;
                line-height: 1.6;
                color: #333;
                margin: 10px 0;
                font-weight: 700;
            }
            
            .core-line span {
                color: var(--primary-pink);
            }
            
            .final-instruction {
                font-size: 1.3rem;
                font-weight: 700;
                color: var(--primary-pink);
                margin-bottom: 20px;
                line-height: 1.6;
            }

            .final-pic-container {
                width: 90%;
                max-width: 550px;
                border-radius: 15px;
                overflow: hidden;
                box-shadow: 0 15px 40px rgba(0,0,0,0.2);
                border: 10px solid white;
                margin-bottom: 40px;
                background-color: #eee;
                transition: max-width 0.4s ease-in-out;
            }
            
            .final-pic-container.phone-frame {
                max-width: 280px;
            }
            .final-pic-container img { width: 100%; height: auto; display: block; }
            
            .final-birthday-msg {
                font-size: 1.6rem;
                font-weight: 800;
                color: var(--text-dark);
                font-family: 'Montserrat', sans-serif;
                line-height: 1.5;
                background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 30px;
            }

            .video-section {
                width: 100%;
                max-width: 600px;
                margin-top: 30px;
                padding-top: 30px;
                border-top: 3px dashed #eee;
                box-sizing: border-box;
            }

            .video-title {
                font-size: 1.8rem;
                font-weight: 800;
                color: var(--primary-purple);
                margin-bottom: 20px;
                font-family: 'Montserrat', sans-serif;
            }

            .video-container {
                width: 100%;
                max-width: 360px; 
                aspect-ratio: 9 / 16; 
                margin: 0 auto; 
                border-radius: 16px; 
                overflow: hidden; 
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
            }

            .video-container video {
                width: 100%;
                height: 100%;
                object-fit: cover; 
            }

            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-12px); }
                60% { transform: translateY(-6px); }
            }
            @keyframes slideDown { from { opacity: 0; transform: translateY(-20px); } to { opacity: 1; transform: translateY(0); } }
            @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
            
        </style>
    </head>
    <body>

        <!-- 1. COUNTDOWN SCREEN -->
        <div id="countdown-screen" class="screen">
            <div id="countdown">5</div>
        </div>

        <!-- 2. MAIN FESTIVAL AREA -->
        <div id="main-content">
            <div class="screen">
                <div class="banner-21">
                    <h2 class="title-21">You Turn 21 on the 21st uh la... Periya aalu thaan!!</h2>
                </div>
                
                <svg class="arc-container" viewBox="0 0 700 140">
                    <defs>
                        <path id="fullSentenceArc" d="M 50,130 A 300,140 0 0,1 650,130" fill="transparent" />
                    </defs>
                    <text class="arc-text">
                        <textPath href="#fullSentenceArc" startOffset="50%" text-anchor="middle">
                            <tspan class="word-happy">HAPPY</tspan> 
                            <tspan class="word-birthday"> BIRTHDAY</tspan>
                            <tspan class="word-ngo"> NGO !!!</tspan>
                        </textPath>
                    </text>
                </svg>

                <div class="profile-pic-container">
                    <img src="{{ url_for('static', filename='jeysri_hbd.jpeg') }}" alt="Birthday Profile Pic" onerror="handleImageError(this)">
                </div>
                
                <div class="scroll-down">
                    <p>Keezha thalli paaru di... 👇</p>
                    <div class="arrow">▼</div>
                </div>
            </div>

            <!-- 3. INTERACTIVE CORNER -->
            <div class="message-section">
                <div class="msg-box">
                    <p class="intro-p"><b>Hey Maazaaa Bottle ehhhh... 😂</b></p>
                    <p class="intro-p">Stay Happy and Stay Strong, Indha B'Day la irundhu new you aaah iru. Ini nee eduthu veikira oru oru step um sumaaa THAGA THAGA nu jolikka indha moonu mattis oda vaazhthukkal ngo 🎉❤️</p>
                    
                    <div class="poem-wrapper">
                        <div class="quote-title">TOWARDS YOU</div>
                        <button id="blast-trigger-btn" class="action-btn" onclick="blastPoem()">💥 BLAST TO READ 💥</button>
                        
                        <div id="poem-content">
                            <p class="quote-line">Struggles in form of Fire that vaporizes into Gas</p>
                            <p class="quote-line">Struggles in form of Rock that crushes into Dust</p>
                            <p class="quote-line">Struggles in form of Human that Disappear like Ghost</p>
                            <p class="quote-line">Struggles Anything will come TOWARDS YOU in form of Anything that Transforms into Nothing</p>
                        </div>
                    </div>
                    
                    <div id="post-blast-box">
                        <p class="surprise-text">"Sandhosama Surprise aairpa nu namburom but inonu iruku, Keezha iruka andha AuraHVN button ah click pani paaru"</p>
                        <button class="aurahvn-btn" onclick="revealGallery()">
                            ⚡ AuraHVN ⚡
                        </button>
                    </div>
                </div>
            </div>

            <!-- 4. GALLERY & VIDEO SECTION -->
            <div id="gallery-section">
                <div class="gallery-box">
                    <h2 class="gallery-question">Una nee epdi paakanum nu aasa padra?</h2>
                    
                    <div class="option-btn-container">
                        <button id="btn-supergirl" class="opt-btn" onclick="showOption('supergirl')">1) SuperGirl</button>
                        <button id="btn-angel" class="opt-btn" onclick="showOption('angel')">2) Angel</button>
                        <button id="btn-homelygirl" class="opt-btn" onclick="showOption('homelygirl')">3) HomelyGirl</button>
                    </div>
                    
                    <div class="display-area">
                        <div id="display-supergirl" class="image-display-wrapper option-display">
                            <img src="{{ url_for('static', filename='Jeysri_SuperGirl.jpeg') }}" alt="SuperGirl Variant" onerror="handleImageError(this)">
                            <div class="img-placeholder" style="display:none;">[ SuperGirl AI Pic Placeholder ]</div>
                        </div>
                        <div id="display-angel" class="image-display-wrapper option-display">
                            <img src="{{ url_for('static', filename='Jeysri_Angel.jpeg') }}" alt="Angel Variant" onerror="handleImageError(this)">
                            <div class="img-placeholder" style="display:none;">[ Angel AI Pic Placeholder ]</div>
                        </div>
                        <div id="display-homelygirl" class="image-display-wrapper option-display">
                            <img src="{{ url_for('static', filename='Jeysri_HomelyGirl.jpeg') }}" alt="HomelyGirl Variant" onerror="handleImageError(this)">
                            <div class="img-placeholder" style="display:none;">[ HomelyGirl AI Pic Placeholder ]</div>
                        </div>
                    </div>
                    
                    <!-- --- FINAL SURPRISE AREA --- -->
                    <div id="final-surprise-area">
                        <div class="core-justification-block">
                            <div class="core-line">1. Nadaka poradhulaam unaku kanavu la vandhrum, adhunaala nee <span>SuperGirl</span>.</div>
                            <div class="core-line">2. Mannikave mudiyaadha vishayathuku, Mannikave koodaadha vishayathuku laam mannichirka, adhunaala nee <span>Angel</span>.</div>
                            <div class="core-line">3. Adikadi kovil pova, Bakthi mode naala nee <span>HomelyGirl</span>.</div>
                        </div>

                        <p class="final-instruction">Keezha paaru unaku oru wallpaper ohh dp ohh vechikira maari oru pic irukum...</p>
                        
                        <!-- DEVICE SELECTOR BUTTONS -->
                        <div class="device-btn-container">
                            <button id="btn-laptop" class="dev-btn active" onclick="swapDeviceView('laptop')">💻 Laptop View</button>
                            <button id="btn-mobile" class="dev-btn" onclick="swapDeviceView('mobile')">📱 Mobile View</button>
                        </div>
                        
                        <div id="wallpaper-wrapper" class="final-pic-container">
                            <img id="final-wallpaper-img" src="{{ url_for('static', filename='Jeysri_Wallpaper_lap.jpg') }}" alt="Birthday Wallpaper" onerror="handleImageError(this)">
                            <div class="img-placeholder" style="display:none;">[ Final Wallpaper AI Pic Placeholder ]</div>
                        </div>

                        <!-- --- NEW VIDEO AREA --- -->
                        <div class="video-section">
                            <h3 class="video-title">🎥 Una Paraka Vechirken Paaru!</h3>
                            <div class="video-container">
                                <video id="birthday-video" controls>
                                    <source src="{{ url_for('static', filename='Jeysri_AI_Video.mp4') }}" type="video/mp4">
                                    Your browser does not support the video tag.
                                </video>
                            </div>
                        </div>
                        
                        <p class="final-birthday-msg" style="margin-top: 40px;">
                            Happy,Shock,Surprise laam aagirpa nu namburom ,<br> once again happy birthday 🎉🎂 by Moonu Mattis
                        </p>
                    </div>
                    
                </div>
            </div>
            
        </div>

        <script>
            let count = 5;
            const countdownEl = document.getElementById('countdown');
            const timer = setInterval(() => {
                count--;
                if (count > 0) {
                    countdownEl.innerText = count;
                } else if (count === 0) {
                    countdownEl.innerText = "🎉 ngo!";
                    countdownEl.style.fontSize = "6rem";
                } else {
                    clearInterval(timer);
                    revealSurprise();
                }
            }, 1000);

            function loopCrackers() {
                var duration = 4 * 1000;
                var end = Date.now() + duration;
                var colors = ['#ff6b6b', '#a55eea', '#4bcffa', '#feca57'];

                (function frame() {
                    confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: colors });
                    confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: colors });
                    if (Date.now() < end) { requestAnimationFrame(frame); }
                }());
            }

            function handleImageError(img) {
                img.style.display = 'none';
                if (img.nextElementSibling) {
                    img.nextElementSibling.style.display = 'flex';
                }
            }

            function revealSurprise() {
                document.getElementById('countdown-screen').style.display = 'none';
                document.getElementById('main-content').style.display = 'block';
                loopCrackers();
            }

            function blastPoem() {
                confetti({ particleCount: 150, spread: 80, origin: { y: 0.6 }, colors: ['#ff6b6b', '#a55eea'] });
                
                document.getElementById('blast-trigger-btn').style.display = 'none';
                document.getElementById('poem-content').style.display = 'block';
                
                setTimeout(() => {
                    document.getElementById('post-blast-box').style.display = 'block';
                    window.scrollBy({ top: 300, behavior: 'smooth' });
                    confetti({ particleCount: 50, spread: 100, origin: { y: 0.8 }, colors: ['#4bcffa', '#feca57'] });
                }, 400);
            }
            
            let clickedOptions = {
                supergirl: false,
                angel: false,
                homelygirl: false
            };

            function revealGallery() {
                document.getElementById('post-blast-box').style.opacity = '0.5';
                document.querySelector('.aurahvn-btn').disabled = true;

                const gallery = document.getElementById('gallery-section');
                gallery.style.display = 'flex';
                gallery.scrollIntoView({ behavior: 'smooth' });
                
                setTimeout(() => {
                   confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 }, colors: ['#a55eea', '#feca57'] });
                }, 500);
            }

            // JavaScript dynamic source URLs also need correct Flask rendering
            const wallpaperLapUrl = "{{ url_for('static', filename='Jeysri_Wallpaper_lap.jpg') }}";
            const wallpaperMobileUrl = "{{ url_for('static', filename='Jeysri_Wallpaper.jpg') }}";

            function showOption(optionId) {
                clickedOptions[optionId] = true;
                
                document.querySelectorAll('.opt-btn').forEach(btn => btn.classList.remove('active'));
                document.getElementById('btn-' + optionId).classList.add('active');

                document.querySelectorAll('.option-display').forEach(div => div.style.display = 'none');
                document.getElementById('display-' + optionId).style.display = 'block';
                
                confetti({ particleCount: 30, spread: 50, origin: { y: 0.7 }, colors: ['#4bcffa'] });

                checkFinalSurprise();
            }

            function swapDeviceView(device) {
                const wallpaperImg = document.getElementById('final-wallpaper-img');
                const wrapper = document.getElementById('wallpaper-wrapper');
                
                document.querySelectorAll('.dev-btn').forEach(btn => btn.classList.remove('active'));
                document.getElementById('btn-' + device).classList.add('active');

                if (device === 'laptop') {
                    wallpaperImg.src = wallpaperLapUrl;
                    wrapper.classList.remove('phone-frame');
                } else if (device === 'mobile') {
                    wallpaperImg.src = wallpaperMobileUrl;
                    wrapper.classList.add('phone-frame');
                }
            }

            function checkFinalSurprise() {
                const allClicked = Object.values(clickedOptions).every(value => value === true);
                
                if (allClicked) {
                    const finalArea = document.getElementById('final-surprise-area');
                    
                    setTimeout(() => {
                        finalArea.style.display = 'flex';
                        finalArea.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        
                        setTimeout(() => {
                             confetti({ 
                                particleCount: 200, 
                                spread: 100, 
                                origin: { y: 0.8 }, 
                                colors: ['#ff6b6b', '#a55eea', '#4bcffa', '#feca57', '#FFFFFF'] 
                            });
                        }, 500);
                        
                    }, 1000);
                }
            }
        </script>
    </body>
    </html>
    """
    # prechana solution: render_template_string kulla context function ah pass pannanum!
return render_template_string(html_content, url_for=url_for)

if __name__ == "__main__":
    app.run(debug=True)