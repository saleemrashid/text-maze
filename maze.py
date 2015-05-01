__all__ = ["Maze"]
from random import shuffle, randrange

def Maze(width, height):
    maze = [None] * height * 2
    maze[::2] = [[True, True] * width + [True] for y in range(height)]
    maze[1::2] = [[True, False] * width + [True] for y in range(height)]
    maze += [[True] * width * 2 + [True]]
    done = [[False] * width for y in range(height)]
    def walk(x, y):
        done[y][x] = True

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)

        for xx, yy in d:
            if xx >= 0 and yy >= 0 and yy < height and xx < width and not done[yy][xx]:
                if xx == x:
                    maze[max(y, yy) * 2][x * 2] = True
                    maze[max(y, yy) * 2][x * 2 + 1] = False
                elif yy == y:
                    maze[y * 2 + 1][max(x, xx) * 2] = False
                    maze[y * 2 + 1][max(x, xx) * 2 + 1] = False
                walk(xx, yy)
    walk(randrange(width), randrange(height))
    return maze
