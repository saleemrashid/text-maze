__all__ = ["getch", "ungetch"]

def _load_getch():
    try:
        # POSIX
        import termios
    except ImportError:
        # Windows
        import msvcrt
        return msvcrt.getch

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

buf = []

def getch():
    if len(buf):
        return buf.pop()
    else:
        return _getch()

def ungetch(c):
    buf.append(c)
