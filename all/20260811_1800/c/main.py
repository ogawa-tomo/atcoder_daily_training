class Grid:
    COLOR_WHITE = "white"
    COLOR_BLACK = "black"

    def __init__(self) -> None:
        self.color = self.COLOR_WHITE

    @property
    def is_white(self):
        return self.color == self.COLOR_WHITE

    @property
    def is_black(self):
        return self.color == self.COLOR_BLACK

    def set_white(self):
        self.color = self.COLOR_WHITE

    def set_black(self):
        self.color = self.COLOR_BLACK

    def __repr__(self) -> str:
        if self.is_white:
            return "."
        else:
            return "#"


H, W, N = map(int, input().split())
grids: list[list[Grid]] = []
for i in range(H):
    row = [Grid() for _ in range(W)]
    grids.append(row)


# print(grids)
class Takahashi:
    def __init__(self) -> None:
        self.i = 0
        self.j = 0
        self.dis = [-1, 0, 1, 0]
        self.djs = [0, 1, 0, -1]
        self.dir_idx = 0

    def turn_right(self):
        self.dir_idx = (self.dir_idx + 1) % 4

    def turn_left(self):
        self.dir_idx = (self.dir_idx - 1) % 4

    def forward(self):
        di = self.dis[self.dir_idx]
        self.i = (self.i + di) % H
        dj = self.djs[self.dir_idx]
        self.j = (self.j + dj) % W


t = Takahashi()
for _ in range(N):
    current_grid = grids[t.i][t.j]
    if current_grid.is_white:
        current_grid.set_black()
        t.turn_right()
        t.forward()
    else:
        current_grid.set_white()
        t.turn_left()
        t.forward()

for r in grids:
    print("".join([str(g) for g in r]))
