H, W, N = map(int, input().split())
grids: list[list[str]] = []
for _ in range(H):
    grids.append(["." for _ in range(W)])
# print(grids)


class Takahashi:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.di = 0  # 上

    def turn_right(self):
        self.di = (self.di + 1) % 4

    def turn_left(self):
        self.di = (self.di - 1) % 4

    def go_straight(self):
        direction = self.directions[self.di]
        di = direction[0]
        dj = direction[1]
        self.i = (self.i + di) % H
        self.j = (self.j + dj) % W


takahashi = Takahashi()

for _ in range(N):
    grid = grids[takahashi.i][takahashi.j]
    if grid == ".":
        grids[takahashi.i][takahashi.j] = "#"
        takahashi.turn_right()
        takahashi.go_straight()
    elif grid == "#":
        grids[takahashi.i][takahashi.j] = "."
        takahashi.turn_left()
        takahashi.go_straight()

for row in grids:
    print("".join(row))
