__all__ = ["getch"]

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

getch = _load_getch()
