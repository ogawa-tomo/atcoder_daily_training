from collections import deque

H, W = map(int, input().split())


class Grid:
    def __init__(self, i: int, j: int, is_white: bool) -> None:
        self.i = i
        self.j = j
        self.is_white = is_white
        self.neighbors: list[Grid] = []
        self.visited = False
        self.is_outer = self.i == 0 or self.i == H - 1 or self.j == 0 or self.j == W - 1


grids: list[list[Grid]] = []
for i in range(H):
    S = list(input())
    row: list[Grid] = []
    for j, s in enumerate(S):
        grid = Grid(i, j, s == ".")
        row.append(grid)
    grids.append(row)

for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if not grid.is_white:
            continue
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for dir in dirs:
            di = dir[0]
            dj = dir[1]
            ii = i + di
            jj = j + dj
            if ii < 0 or H - 1 < ii or jj < 0 or W - 1 < jj:
                continue
            neighbor = grids[ii][jj]
            if neighbor.is_white:
                grid.neighbors.append(neighbor)

answer = 0
hoge = 0
for i in range(H):
    for j in range(W):
        grid = grids[i][j]
        if not grid.is_white:
            continue
        if grid.visited:
            continue
        is_outer = grid.is_outer
        d: deque[Grid] = deque()
        d.append(grid)
        grid.visited = True
        while d:
            grid = d.popleft()
            for neighbor in grid.neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    is_outer = is_outer or neighbor.is_outer
                    d.append(neighbor)
        if not is_outer:
            answer += 1
print(answer)
