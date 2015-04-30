from getch import getch, ungetch

ARROW_UP = "\x1b[A"
ARROW_DOWN = "\x1b[B"
ARROW_RIGHT = "\x1b[C"
ARROW_LEFT = "\x1b[D"

def get():
    c = getch()
    if c == "\x1b":
        getch()
        return "\x1b[%s" % getch()
    elif c == "\xe0":
        return "\x1b[%s" % getch()
    else:
        return c
