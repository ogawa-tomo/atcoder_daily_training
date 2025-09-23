import math
from collections import deque

N, M = map(int, input().split())


class Grid:
    def __init__(self) -> None:
        self.distance = -1
        self.neighbors: list[Grid] = []


grids: list[list[Grid]] = []
for _ in range(N):
    row: list[Grid] = []
    for _ in range(N):
        row.append(Grid())
    grids.append(row)

# タテにa, ヨコにb
vectors: list[list[int]] = []
for a in range(math.floor(math.sqrt(M)) + 1):
    b = math.sqrt(M - a**2)
    if b.is_integer():
        vectors.append([a, int(b)])
        vectors.append([-a, int(b)])
        vectors.append([a, -int(b)])
        vectors.append([-a, -int(b)])

for i in range(N):
    for j in range(N):
        grid = grids[i][j]
        for vector in vectors:
            a = vector[0]
            b = vector[1]
            if 0 <= i + a and i + a < N and 0 <= j + b and j + b < N:
                neighbor = grids[i + a][j + b]
                grid.neighbors.append(neighbor)

d: deque[Grid] = deque()

start = grids[0][0]
d.append(start)
start.distance = 0
while d:
    grid = d.popleft()
    distance = grid.distance
    for neighbor in grid.neighbors:
        if neighbor.distance == -1:
            d.append(neighbor)
            neighbor.distance = distance + 1

for i in range(N):
    row = grids[i]
    print(" ".join([str(grid.distance) for grid in row]))
