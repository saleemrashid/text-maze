#!/usr/bin/env python3
#
# text-maze
#

import controls
from controls import ARROW_UP, ARROW_LEFT, ARROW_DOWN, ARROW_RIGHT
from maze import Maze
import os

keys = {
    "w": ARROW_UP,
    "a": ARROW_LEFT,
    "s": ARROW_DOWN,
    "d": ARROW_RIGHT
}

def key_transform(c):
    c = c.lower() if len(c) == 1 else c
    return keys[c] if c in keys else c

ASCII_PLAYER = "O "
ASCII_WALL_H = "| "
ASCII_WALL_V = "- "
ASCII_JUNC   = "+ "
ASCII_BLANK  = "  "
ANSI_NORMAL  = "\x1b[47;1m" if os.name == "posix" else ""
ANSI_WALL    = "\x1b[30;40m" if os.name == "posix" else ""
ANSI_PLAYER  = "\x1b[43;33m" if os.name == "posix" else ""
ANSI_RESET   = "\x1b[0;0m" if os.name == "posix" else ""

def draw(maze, px, py):
    player = (px, py)
    for y, row in enumerate(maze):
        for x, status in enumerate(row):
            color = ANSI_NORMAL
            cell = ASCII_BLANK

            if player == (x, y):
                cell = ASCII_PLAYER
                color = ANSI_PLAYER
            elif status:
                color = ANSI_WALL
                left = False if x == 0 else row[x - 1]
                right = False if x + 1 == len(row) else row[x + 1]
                above = False if y == 0 else maze[y - 1][x]
                below = False if y + 1 == len(maze) else maze[y + 1][x]
                v = above or below
                h = left or right

                if v and h:
                    cell = ASCII_JUNC
                elif v:
                    cell = ASCII_WALL_H
                elif h:
                    cell = ASCII_WALL_V
                elif y % 2 == 0:
                    cell = ASCII_WALL_V
                else:
                    cell = ASCII_WALL_H

            print(color, end="")
            print(cell, end="")
            print(ANSI_RESET, end="")
        print()

def verify(maze, player):
    return player[0] >= 0 and player[1] >= 0 and len(maze) > player[1] and len(maze[player[1]]) > player[0] and not maze[player[1]][player[0]]

def move(c, maze, player):
    old = player[:]

    if c == ARROW_UP:
        player[1] -= 1
    elif c == ARROW_DOWN:
        player[1] += 1
    elif c == ARROW_LEFT:
        player[0] -= 1
    elif c == ARROW_RIGHT:
        player[0] += 1

    if not verify(maze, player):
        player[:] = old

def clear():
    print(ANSI_RESET)
    os.system("clear") if os.name == "posix" else os.system("cls")

def main():
    maze = Maze(16, 8)
    frees = []
    for y, row in enumerate(maze):
        for x, wall in enumerate(row):
            if not wall:
                frees.append((x, y))

    player = [0, 0]
    end = [0, 0]
    player[0], player[1] = frees[0]
    end = list(frees[-1])

    while True:
        clear()
        draw(maze, *player)

        if player == end:
            break

        c = key_transform(controls.get())
        move(c, maze, player)


if __name__ == "__main__":
    main()
