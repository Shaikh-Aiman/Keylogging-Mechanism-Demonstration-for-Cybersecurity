# Prerequisites

<p align="center">
  <img src="https://github.com/user-attachments/assets/1ad4a276-ebbe-455a-ac77-7511d17266a8" alt="REQ IMG 1"
       width="500">
</p>


This document explains the system, software, and library requirements needed to run the __DOS Attack Simulator__ successfully.
<br>

---

## Python Dependency File

The project uses a separate `requirements.txt` file for installing dependencies using `pip`.

__Ensure you have the following Python packages installed:__ <br>

- __os:__ Provides access to operating system functionalities such as file handling and directory management.
- __time:__ Used to control execution timing and implement time-limited monitoring.
- __base64:__ Encodes files into Base64 format for safe transmission as email attachments.
- __tkinter:__ Creates graphical user interfaces for consent prompts and user confirmations.
- __tkinter.messagebox:__ Displays popup dialogs for consent, alerts, and confirmation messages.
- __pynput:__ Captures keyboard keystrokes and mouse movement events from the system.
- __pyscreenshot:__ Takes screenshots of the user’s screen programmatically.
- __sounddevice:__ Records audio input from the system microphone.
- __scipy.io.wavfile:__ Saves recorded audio data into WAV file format.
- __requests:__ Sends HTTPS requests to the Mailtrap Sandbox API for email simulation.
- __cv2 (OpenCV):__ Captures a single image frame from the system webcam.
- __sys:__ Handles command-line arguments such as --help and --delete-logs.

<p align="center">
  <img src="https://github.com/user-attachments/assets/14efa349-abff-49da-8c76-72f3bd15eb70" alt="b" width="700">
</p>

