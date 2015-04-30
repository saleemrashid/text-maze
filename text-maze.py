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

ASCII_PLAYER = "X"
ASCII_WALL = "#"
ASCII_BLANK = " "

import os

def draw(maze, px, py):
    player = (px, py)
    for y, row in enumerate(maze):
        for x, status in enumerate(row):
            if player == (x, y):
                print(ASCII_PLAYER, end="")
            else:
                print(ASCII_WALL if status else ASCII_BLANK, end="")
        print()

def clear():
    os.system("clear") if os.name == "posix" else os.system("cls")

def main():

    maze = [[1,1,1],[1,1,1],[1,1,1]]
    player = [0, 0]

    while True:
        clear()
        draw(maze, *player)

        c = key_transform(controls.get())
        if c == ARROW_UP:
            player[1] -= 1
        elif c == ARROW_DOWN:
            player[1] += 1
        elif c == ARROW_LEFT:
            player[0] -= 1
        elif c == ARROW_RIGHT:
            player[0] += 1

if __name__ == "__main__":
    main()
