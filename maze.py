def Maze(width, height):
    maze = [[True] * width] + [[True] + [False] * (width - 2) + [True] for row in range(height - 2)] + [[True] * width]
    maze[1][0] = maze[-2][-1] = False
    return maze
