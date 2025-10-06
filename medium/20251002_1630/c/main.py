H, W, N = map(int, input().split())


class Direction:
    def __init__(self):
        self.directions = ["right", "below", "left", "above"]
        self.current = "above"

    def turn_right(self):
        self.current = self.directions[(self.directions.index(self.current) + 1) % 4]

    def turn_left(self):
        self.current = self.directions[(self.directions.index(self.current) - 1) % 4]


class Grid:
    def __init__(self) -> None:
        self.color = "."
        self.neighbor: dict[str, Grid] = {}

    def __repr__(self):
        return self.color

    def is_white(self):
        return self.color == "."

    def is_black(self):
        return self.color == "#"

    def paint_white(self):
        self.color = "."

    def paint_black(self):
        self.color = "#"


grids: list[list[Grid]] = []
for h in range(H):
    row = [Grid() for _ in range(W)]
    grids.append(row)

for h in range(H):
    for w in range(W):
        grid = grids[h][w]
        grid.neighbor["right"] = grids[h][(w + 1) % W]
        grid.neighbor["left"] = grids[h][(w - 1) % W]
        grid.neighbor["above"] = grids[(h - 1) % H][w]
        grid.neighbor["below"] = grids[(h + 1) % H][w]

direction = Direction()
current_grid = grids[0][0]
for _ in range(N):
    if current_grid.is_white():
        current_grid.paint_black()
        direction.turn_right()
    elif current_grid.is_black():
        current_grid.paint_white()
        direction.turn_left()
    current_grid = current_grid.neighbor[direction.current]

for row in grids:
    print("".join([str(grid) for grid in row]))
