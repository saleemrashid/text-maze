__all__ = ["getch", "ungetch"]
from collections import deque

def _load_getch():
    try:
        # POSIX
        import termios
    except ImportError:
        # Windows
        import msvcrt
        def _getch():
            return chr(ord(msvcrt.getch()))
        return _getch

    # POSIX
    import sys, tty
    def _getch():
        fd = sys.stdin.fileno()
        restore = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, restore)
        return ch

    return _getch

_getch = _load_getch()

buf = deque()

def getch():
    if len(buf):
        return buf.pop()
    else:
        return _getch()

def ungetch(c):
    buf.appendleft(c)
