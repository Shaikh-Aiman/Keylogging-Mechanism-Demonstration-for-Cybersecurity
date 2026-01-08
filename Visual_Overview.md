# This document provides a step-by-step visual walkthrough of the __Keylogging Mechanism Demonstration for Cybersecurity__ project.

### 1. Program Help & Usage Instructions:

- The `--help` command provides a clear overview of how to use the application, including execution, log deletion, and ethical notes.
- This ensures users understand the available options before running any monitoring activity.
- Command used:

       python main.py --help

<p align="center">  <img width="1594" height="465" alt="Screenshot 2026-01-08 224017" src="https://github.com/user-attachments/assets/a419cc17-8937-4602-b3c4-c0f2e33eb87f">
</p>

### 2. User Consent Prompt (Ethical Safeguard):

= Before any monitoring begins, the program displays a GUI consent dialog.
- No data is collected unless the user explicitly clicks __Yes__.
- This step enforces __ethical compliance__ and __transparency__.

<p align="center">  <img width="487" height="369" alt="Screenshot 2026-01-08 223901" src="https://github.com/user-attachments/assets/eb875468-033e-4bcd-9ddb-8e6de842032e">
</p>

### 3. Monitoring Execution (Console Output):
- Once consent is granted, the program begins endpoint monitoring for a fixed duration.
- The console clearly logs the execution status.
- __Activities performed:__
     - Keyboard input logging
     - Mouse movement logging
     - Screenshot capture
     - Microphone recording
     - Webcam image capture
 
<p align="center"> <img width="774" height="187" alt="Screenshot 2026-01-08 223937" src="https://github.com/user-attachments/assets/b5e8ce71-a0fc-461b-b305-b5fac1d14a3c"> </p>

### 4. Log Files Generated Locally:

- All collected data is stored locally in the `logs/` directory.
- This demonstrates how endpoint activity can be aggregated into multiple artifacts.
- Files generated:
     - `keys.txt`
     - `mouse.txt`
     - `audio.wav`
     - `screenshot.png`
     - `webcam.jpg`
     - `activity_report.txt`

<p align="center"> <img width="909" height="386" alt="Screenshot 2026-01-08 224108" src="https://github.com/user-attachments/assets/5e57bf10-4dfd-40df-87b7-0fa91fc388d1">
</p>

### 5. Activity Report Attachment (Mailtrap Sandbox):

- After execution, a consolidated report is sent via Mailtrap Sandbox API.
- This safely simulates how attackers could receive data without using real email servers.
- __Key point:__ Only a sandbox inbox is used to maintain ethical boundaries, ensuring that no real emails are delivered externally and no actual data leakage occurs.
  
<p align="center"> <img width="1203" height="523" alt="Screenshot 2026-01-08 230033" src="https://github.com/user-attachments/assets/514aa693-bcb8-4461-ba5d-c7236073617d"> </p>

### 6. Manual Log Deletion (CLI + GUI Controlled):

- The command  `--delete-logs` provides a command-line option to delete all collected logs.
- This action requires explicit GUI confirmation, preventing accidental deletion.
- Command used:

       python main.py --delete-logs

<p align="center"> <img width="425" height="306" alt="Screenshot 2026-01-08 224148" src="https://github.com/user-attachments/assets/6b53d48b-09b3-48ff-9d7d-a1cf8146e739"> </p>

### 7. Logs Successfully Removed:

- After confirmation, all collected files are permanently removed from the system.
- This demonstrates user control over sensitive data.

 <p align="center"> <img width="1125" height="236" alt="Screenshot 2026-01-08 224217" src="https://github.com/user-attachments/assets/be8295d9-6d3c-4865-b425-1170af4da99a"> </p>



