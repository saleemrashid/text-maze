#!/usr/bin/env python3
#
# text-maze
#

import controls
from controls import ARROW_UP, ARROW_LEFT, ARROW_DOWN, ARROW_RIGHT

def main():
    while True:
        c = controls.get()
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
