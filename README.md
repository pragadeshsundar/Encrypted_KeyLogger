# 🔐 Encrypted Keylogger with Daily Key Rotation

A Python-based keylogger that captures keyboard input, encrypts the keystrokes using Fernet (AES), and stores them in daily log files. The encryption key rotates daily for added security.

---

## 📌 Features

- ⌨️ Captures all keyboard input using `pynput`
- 🔐 AES-based encryption using `cryptography.fernet`
- 🗓 Daily log and key file rotation (logs are stored per day)
- 📂 Encrypted logs saved in `keylogs_encrypted_YYYY-MM-DD.txt`
- 🗝 Unique encryption keys saved as `secret_YYYY-MM-DD.key`
- 🧠 Minimal, self-contained, and easy to run

---

## ⚠️ Disclaimer

This tool is created for **educational and ethical** purposes **only**. Do not use this software to record keystrokes on systems you do not own or do not have explicit permission to monitor. Unauthorized use may violate privacy laws and result in criminal penalties.

---

## 🛠 Requirements

Install the required libraries using pip:

``bash

pip install pynput cryptography

---
## 🚀 How to Run

python keylogger.py

---
# 🔓 Keylogger Log Decryptor

This is a companion script to the **Encrypted Keylogger** project. It reads the encrypted keystroke log generated for **today's date**, decrypts it using the corresponding daily key, and prints the decrypted keystrokes to the console.

---

## 📦 Features

- 📅 Automatically selects today’s encrypted log file and matching encryption key
- 🔐 Decrypts AES-encrypted logs using Fernet (symmetric encryption)
- 🧾 Displays readable keystroke logs for review or debugging

---

## 🛠 Requirements

Install dependencies:

``bash
pip install cryptography

---
## 🚀 How to Use

python decrypt.py

## Sample Output

🔓 Decrypted log for 2025-07-04:

[2025-07-04 13:40:21] Hello world
[2025-07-04 13:41:02] password123
...

---

##⚠️ Troubleshooting

- Missing key file?
  The script will alert you if secret_YYYY-MM-DD.key is not found.

- Missing log file?
  It will also notify if keylogs_encrypted_YYYY-MM-DD.txt is missing.

- Error decrypting line?
  If a line in the file is corrupted or mismatched with the key, an error message will be printed.

---


