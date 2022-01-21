import sys
import os

def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            import msvcrt
        except ImportError:
            raise ImportError('getch not available')
        else:
            key = msvcrt.getwch()
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')