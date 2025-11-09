"""
Remote controller with:
✅ Passcode login page (8072)
✅ Timed Wi-Fi cut
✅ Screenshot every 2 seconds
✅ Modern GUI
✅ ngrok tunnel with your authtoken

RUN AS ADMIN:
    Right-click CMD → Run as administrator
    python remote_controller_full.py
"""

from flask import Flask, request, send_file, redirect, render_template_string, session
import os, time, threading
import pyautogui
from pyngrok import ngrok
from PIL import Image

# ================================
# Config
# ================================
NGROK_AUTHTOKEN = "35EXrX5HNxLQXEko1ybnEPQBH5r_2ssQQWcpydYG6SAFaoNdz"
PORT = 5000

# webpage passcode
PASSCODE = "8072"

# secret key for screenshot/cut API
SECRET = "MY_SUPER_SECRET_19238712398123"

# Wi-Fi interface
WIFI_NAME = "Wi-Fi"

SCREENSHOT_PATH = "screen.jpg"

# Flask session secret
app = Flask(__name__)
app.secret_key = "this_is_session_key_change_later"

# ================================
# Internet Toggle
# ================================
def disable_wifi():
    os.system(f'netsh interface set interface name="{WIFI_NAME}" admin=disabled')

def enable_wifi():
    os.system(f'netsh interface set interface name="{WIFI_NAME}" admin=enabled')

def cut_internet_for(seconds: int):
    print(f"[CUT] Wi-Fi off for {seconds}s")
    disable_wifi()
    time.sleep(seconds)
    enable_wifi()
    print("[CUT] Wi-Fi Enabled again")

# ================================
# Screenshot
# ================================
def save_screenshot(path):
    img = pyautogui.screenshot()

    # Resize screenshot to medium size
    w = int(img.width * 0.6)
    h = int(img.height * 0.6)
    img = img.resize((w, h))

    img.save(path, "JPEG", quality=60, optimize=True)

# ================================
# HTML Templates
# ================================

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Login</title>
  <style>
    body { 
      font-family: Arial; 
      display:flex; justify-content:center; align-items:center; height:100vh;
      background:#121212; color:white;
    }
    .box {
      padding:30px;
      background:#1f1f1f;
      border-radius:10px;
      text-align:center;
      width:300px;
    }
    input {
      width:90%;
      padding:10px;
      margin-top:10px;
      border-radius:5px;
      border:none;
      font-size:16px;
    }
    button {
      margin-top:15px;
      width:95%;
      padding:10px;
      font-size:16px;
      background:#4CAF50;
      border:none;
      color:white;
      border-radius:5px;
      cursor:pointer;
    }
  </style>
</head>
<body>
  <div class="box">
    <h2>Enter Passcode</h2>
    <form method="POST">
      <input type="password" name="passcode" placeholder="Passcode">
      <button type="submit">Enter</button>
    </form>
    {% if error %}<p style="color:red;">Incorrect Passcode</p>{% endif %}
  </div>
</body>
</html>
"""

DASHBOARD_PAGE = """
<!DOCTYPE html>
<html>
<head>
  <title>Remote Dashboard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body { 
        font-family: Arial; 
        padding:20px; 
        background:#111; 
        color:white;
        text-align:center;
    }
    .card {
        background:#1b1b1b;
        padding:20px;
        border-radius:10px;
        max-width:650px;
        margin:0 auto;
    }
    input {
        width:150px;
        padding:10px;
        font-size:18px;
        border-radius:5px;
        border:none;
    }
    button {
        padding:10px 20px;
        font-size:18px;
        margin-left:10px;
        background:#ff4444;
        border:none;
        color:white;
        border-radius:5px;
        cursor:pointer;
    }
    img {
        margin-top:20px;
        max-width:95%;
        border:2px solid #333;
        border-radius:5px;
    }
    #statusBox {
        margin-top:15px;
        font-size:20px;
        font-weight:bold;
    }
  </style>
</head>
<body>

  <h2>Remote Internet Controller</h2>

  <div class="card">

      <div id="statusBox">Checking status...</div>

      <br>

      <input id="sec" type="number" placeholder="Seconds" min="1">
      <button onclick="cutInternet()">CUT INTERNET</button>

      <p id="msg"></p>
      <p id="wifiStatus" style="font-size:18px; color:#ff4444;"></p>

      <h3>Live Screen</h3>
      <img id="scr" src="/screen.jpg?key={{secret}}&_={{ts}}">
  </div>

<script>
const SECRET = "{{secret}}";
let wifiRemaining = 0;
let wifiInterval = null;

function cutInternet() {
    let s = document.getElementById("sec").value;
    if (!s) return alert("Enter seconds!");

    fetch(`/cut?time=${s}&key=${SECRET}`)
      .then(r => r.text())
      .then(t => {
        document.getElementById("msg").innerText = t;

        // Start countdown
        wifiRemaining = parseInt(s);
        updateWiFiStatus();

        if (wifiInterval) clearInterval(wifiInterval);
        wifiInterval = setInterval(() => {
            wifiRemaining--;
            updateWiFiStatus();
            if (wifiRemaining <= 0) {
                clearInterval(wifiInterval);
                wifiRemaining = 0;
                document.getElementById("wifiStatus").innerText = "Wi-Fi is ON ✅";
                document.getElementById("wifiStatus").style.color = "#00ff00";
            }
        }, 1000);
      });
}

function updateWiFiStatus() {
    if (wifiRemaining > 0) {
        document.getElementById("wifiStatus").innerText =
            "Wi-Fi is OFF — " + wifiRemaining + "s remaining";
        document.getElementById("wifiStatus").style.color = "#ff4444";
    } else {
        document.getElementById("wifiStatus").innerText = "Wi-Fi is ON ✅";
        document.getElementById("wifiStatus").style.color = "#00ff00";
    }
}

// -----------------------
// PC ONLINE/OFFLINE STATUS
// -----------------------
function checkPCStatus() {
    let img = document.getElementById("scr");

    fetch(img.src)
      .then(r => {
        document.getElementById("statusBox").innerText = "PC Status: ONLINE ✅";
        document.getElementById("statusBox").style.color = "#00ff00";
      })
      .catch(e => {
        document.getElementById("statusBox").innerText = "PC Status: OFFLINE ❌";
        document.getElementById("statusBox").style.color = "#ff4444";
      });
}

// Refresh screenshot
setInterval(() => {
    document.getElementById("scr").src = `/screen.jpg?key=${SECRET}&_=` + Date.now();
    checkPCStatus();
}, 2000);

// Initial state
updateWiFiStatus();
checkPCStatus();
</script>

</body>
</html>
"""


# ================================
# Routes
# ================================

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form.get("passcode") == PASSCODE:
            session["logged"] = True
            return redirect("/dashboard")
        return render_template_string(LOGIN_PAGE, error=True)

    return render_template_string(LOGIN_PAGE, error=False)

@app.route("/dashboard")
def dashboard():
    if not session.get("logged"):
        return redirect("/")
    return render_template_string(DASHBOARD_PAGE, secret=SECRET, ts=int(time.time()))

@app.route("/cut")
def cut_endpoint():
    if request.args.get("key") != SECRET:
        return "Unauthorized", 401

    sec = request.args.get("time")
    if not sec or not sec.isdigit():
        return "Invalid time"

    sec = int(sec)

    threading.Thread(target=cut_internet_for, args=(sec,), daemon=True).start()
    return f"Wi-Fi will be OFF for {sec} seconds."

@app.route("/screen.jpg")
def screen_route():
    if request.args.get("key") != SECRET:
        return "Unauthorized", 401

    save_screenshot(SCREENSHOT_PATH)
    return send_file(SCREENSHOT_PATH, mimetype="image/jpeg")

# ================================
# Start ngrok + Flask
# ================================
if __name__ == "__main__":
    print("[ngrok] Starting tunnel...")
    ngrok.set_auth_token(NGROK_AUTHTOKEN)
    url = ngrok.connect(PORT, "http")
    print("PUBLIC URL:", url)
    print("Run this script as ADMIN!")
    app.run(port=PORT, host="0.0.0.0")
