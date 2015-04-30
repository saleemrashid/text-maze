from getch import getch, ungetch

ARROW_UP = "\x1b[A"
ARROW_DOWN = "\x1b[B"
ARROW_RIGHT = "\x1b[C"
ARROW_LEFT = "\x1b[D"

def get():
    c = getch()
    if c == "\x1b":
        # POSIX
        getch()
        return "\x1b[%s" % getch()
    elif c == "\xe0" or c == "\x00":
        # Windows
        d = ord(getch())
        if d == 72:
            return ARROW_UP
        elif d == 80:
            return ARROW_DOWN
        elif d == 75:
            return ARROW_LEFT
        elif d == 77:
            return ARROW_RIGHT
        else:
            return "%s%s" % (c, chr(d))
    else:
        return c
