#!/usr/bin/env python3
#
# text-maze
#

import controls
from controls import ARROW_UP, ARROW_LEFT, ARROW_DOWN, ARROW_RIGHT

keys = {
    "w": ARROW_UP,
    "a": ARROW_LEFT,
    "s": ARROW_DOWN,
    "d": ARROW_RIGHT
}

def key_transform(c):
    c = c.lower() if len(c) == 1 else c
    return keys[c] if c in keys else c

def main():
    while True:
        c = key_transform(controls.get())

        if c == ARROW_UP:
            print("up")
        elif c == ARROW_LEFT:
            print("left")
        elif c == ARROW_RIGHT:
            print("right")
        elif c == ARROW_DOWN:
            print("down")
        else:
            print(repr(c))

if __name__ == "__main__":
    main()
