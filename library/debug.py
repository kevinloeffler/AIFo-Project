from colorama import Fore, Style

def init(mode):
    global DEBUG_MODE
    DEBUG_MODE = mode

def log(message):
    if DEBUG_MODE:
        print(Fore.YELLOW + 'DEBUG: ' + str(message) + Style.RESET_ALL)
