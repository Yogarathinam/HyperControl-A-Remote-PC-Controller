HyperControl – Remote PC Controller
===================================

HyperControl is a lightweight, self-hosted remote PC control system that runs on Windows and gives you secure access to your computer from anywhere in the world using only a browser.

It is built for flexibility, privacy, and future expansion — allowing you to perform key actions on your PC even if you are far away from it.

🚀 Why HyperControl Exists
--------------------------

Most remote desktop tools (TeamViewer, AnyDesk, Chrome Remote Desktop):

*   Require heavy installation
    
*   Sometimes block sessions or disconnect
    
*   Depend on third-party servers
    
*   Don’t give low-level access to system functions
    
*   Aren’t fully customizable
    

**HyperControl gives you:**
✅ Full control
✅ Self-hosted privacy
✅ Fast setup (no port forwarding)
✅ Easy customization
✅ Runs as a small Python agent
✅ Debug-friendly console output

**This tool is perfect for:**

*   Students
    
*   Developers
    
*   Travelers
    
*   Home PC users
    
*   IT admins
    
*   Automation enthusiasts
    
*   Privacy-focused users
    
*   Security researchers
    

✅ Current Features
------------------

### 🔐 1. Password-Protected Dashboard

A login page appears first.

**Default passcode: 8072**

(You can change this inside the script.)

### 📡 2. Timed Wi-Fi Kill-Switch

You can turn off your PC’s Wi-Fi for X seconds, and it will automatically reconnect.

Useful if you:

*   Want to temporarily block downloads
    
*   Want to stay safe on a public network
    
*   Want to force apps offline
    
*   Want to disable internet while still keeping remote access via the timer
    

### 🖥️ 3. Live Screenshot Streaming (1 frame every 2 seconds)

*   See your desktop in near-real time
    
*   Compressed screenshots for fast loading
    
*   Works even on mobile internet
    
*   Helps you monitor what your PC is doing
    

### ✅ 4. PC Online/Offline Status Indicator

*   🟢 **ONLINE** = PC is responding and screenshot loads
    
*   🔴 **OFFLINE** = PC disconnected or Wi-Fi temporarily off
    

### ⏳ 5. Live Wi-Fi Countdown

When Wi-Fi is disabled, the panel shows:

> Wi-Fi is OFF — 25s remaining

When finished:

> ✅ Wi-Fi is ON

### 🛠 6. No Port Forwarding Needed (ngrok Integration)

HyperControl uses ngrok to create a secure public URL that connects directly to your PC.

This means:✅ Works anywhere✅ Even behind NAT✅ No router changes✅ No need for static IP

### 🪟 7. One-click Start via BAT File

Included file:

run\_hypercontrol\_elevated.bat

This automatically:✅ Checks for Admin rights✅ Elevates via UAC✅ Starts the server✅ Shows real-time GET/POST logs (for debugging)

Perfect for running HyperControl easily.

📦 Installation & Setup
-----------------------

### ✅ 1. Install Python

Download Python 3.10 or newer:👉 https://www.python.org/downloads/

Check installation:
`   python --version   `

### ✅ 2. Install Required Dependencies

Run:

`   pip install flask pyngrok pyautogui pillow   `

### ✅ 3. Place the Files

Your folder should look like:

   HyperControl-RemotePC/  
      │  ├── remote_controller.py  
         └── run_hypercontrol_elevated.bat   

Make sure both files are in the same directory.

### ✅ 4. Setup ngrok (Important)

**Step 1 — Create a free ngrok account**https://ngrok.com/signup

**Step 2 — Get your Authtoken**Dashboard → Your Authtoken

**Step 3 — Add token in the script**Inside remote\_controller.py:

`   NGROK_AUTHTOKEN = "YOUR_TOKEN"   `

### ✅ 5. Running HyperControl

**Important:**
🚨 You must run this with **Administrator privileges**, because netsh (Wi-Fi control) requires it.

**✅ Start HyperControl using the BAT file**

Double-click:

`run\_hypercontrol\_elevated.bat`

It will:

1.  Request Admin privileges
    
2.  Start the Python server
    
3.  Start ngrok
    
4.  Show real-time logs
    
5.  Print a public URL like:https://abcd1234.ngrok-free.app
    

### ✅ 6. Accessing Your Remote PC

1.  Open the ngrok public URL
    
2.  You will see the passcode login page
    
3.  Enter passcode: 8072
    
4.  The dashboard opens
    

From here you can:✅ View live screenshots✅ Cut Wi-Fi for X seconds✅ See countdown timer✅ Monitor online/offline status

Use your mobile, laptop, or any browser.

🔐 Security Notes
-----------------

⚠️ Change the dashboard passcode (8072) to something stronger.
⚠️ Change the SECRET\_KEY in the script before exposing publicly.
⚠️ Never share your ngrok public URL with strangers.
⚠️ Treat your ngrok authtoken like a password.

⚠️ **Recommended:**

*   Set your repo to **Private** to avoid leaks.
    

🛠 Troubleshooting
------------------

**✅ Wi-Fi toggle not working?**

*   You didn’t run the script as Admin.
    
*   Run the BAT file — it will elevate automatically.
    

**✅ Screenshot not loading?**

*   PC might be offline or Wi-Fi was cut.
    
*   After the timer ends, it will reconnect automatically.
    

**✅ Ngrok URL not appearing?**

*   Your authtoken is missing or invalid.
    
*   Update the token inside the script.
    

**✅ "python not recognized"**

*   You need to add Python to PATH during installation or use:py remote\_controller.py
    

🚀 Future Improvements (Roadmap)
--------------------------------

*   ✅ **Remote Mouse Control**
    
    *   Move cursor
        
    *   Left/right click
        
    *   Drag & drop
        
*   ✅ **Remote Keyboard Control**
    
    *   Type text
        
    *   Hotkeys (CTRL+C, ALT+TAB)
        
*   ✅ **Webcam Snapshot Mode**
    
    *   Capture photo
        
    *   Stream webcam at intervals
        
*   ✅ **System Status Panel**
    
    *   CPU usage
        
    *   RAM usage
        
    *   Disk usage
        
    *   Battery percentage
        
    *   Temperature
        
*   ✅ **File Explorer**
    
    *   List directories
        
    *   Download files
        
    *   Upload files
        
*   ✅ **Remote Command Executor**
    
    *   Run PowerShell / CMD commands
        
    *   Return output
        
*   ✅ **Real-Time Video Streaming**
    
    *   MJPEG or WebRTC
        
    *   Live 10–30 FPS feed
        
*   ✅ **Multi-PC Support**
    
    *   Connect multiple PCs to a single dashboard
        
    *   Dropdown for switching PCs
        
*   ✅ **Mobile App Version**
    
    *   Android app
        
    *   Push notifications
        
    *   Quick actions
        

❤️ Why HyperControl is Different
--------------------------------

HyperControl focuses on:
✅ **Privacy** — self-hosted
✅ **Simplicity** — one Python script
✅ **Security** — login + secret keys
✅ **Flexibility** — easily extendable
✅ **Speed** — minimal overhead
✅ **Transparency** — you see logs in real-time

HyperControl gives you something commercial remote tools don’t:**Complete control over your own device.**

📜 License
----------


   ✅ **MIT** 
    
  
    

✅ **End**

Thank you for using HyperControl – Remote PC Controller.

This is just the beginning — many powerful features are coming next.

For new feature requests, improvements, or issues, create an issue on GitHub.
