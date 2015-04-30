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

def draw(maze, player):
    for x, column in enumerate(maze):
        for y, status in enumerate(column):
            if player == (x, y):
                print(ASCII_PLAYER, end="")
            else:
                print(ASCII_WALL if status else ASCII_BLANK, end="")
        print()

def clear():
    os.system("clear") if os.name == "posix" else os.system("cls")

def main():
    clear()

    maze = [[1,1,1],[1,1,1],[1,1,1]]
    player = (0, 0)

    draw(maze, player)

if __name__ == "__main__":
    main()
