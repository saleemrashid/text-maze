__all__ = ["Maze"]
from random import shuffle, randrange

def Maze(width, height):
    v = [["#", " "] * width for y in range(height)]
    h = [["#", "#"] * width for y in range(height)]
    done = [[False] * width for y in range(height)]
    def walk(x, y):
        done[y][x] = True

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)

        for xx, yy in d:
            if xx >= 0 and yy >= 0 and yy < height and xx < width and not done[yy][xx]:
                if xx == x:
                    h[max(y, yy)][x * 2] = "#"
                    h[max(y, yy)][x * 2 + 1] = " "
                elif yy == y:
                    v[y][max(x, xx) * 2] = " "
                    v[y][max(x, xx) * 2 + 1] = " "
                walk(xx, yy)
    walk(randrange(width), randrange(height))
    for a, b in zip(h, v):
        print("".join(a + ["\n"] + b))
    return maze
