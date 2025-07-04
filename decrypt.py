from cryptography.fernet import Fernet
from datetime import datetime
import os

def decrypt_today_log():
    # Get today's date
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Define filenames
    key_file = f"secret_{date_str}.key"
    log_file = f"keylogs_encrypted_{date_str}.txt"

    # Check if key file exists
    if not os.path.exists(key_file):
        print(f"[!] Key file for {date_str} not found.")
        return

    # Check if log file exists
    if not os.path.exists(log_file):
        print(f"[!] Log file for {date_str} not found.")
        return

    # Load AES key
    with open(key_file, 'rb') as f:
        key = f.read()

    fernet = Fernet(key)

    # Decrypt and print each line
    print(f"\n🔓 Decrypted log for {date_str}:\n")
    with open(log_file, 'rb') as f:
        for line in f:
            try:
                decrypted = fernet.decrypt(line.strip()).decode()
                print(decrypted)
            except Exception as e:
                print(f"[Error decrypting line] {e}")

if __name__ == '__main__':
    decrypt_today_log()
