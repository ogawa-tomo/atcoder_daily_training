from dataclasses import dataclass

N = int(input())


@dataclass
class Coords:
    x: int
    y: int


grids: list[list[bool]] = []
for _ in range(N):
    A = list(input())
    row: list[bool] = []
    for a in A:
        row.append(a == "#")
    grids.append(row)


# ローテする前の座標
def before_coords(coords: Coords):
    return Coords(N - 1 - coords.y, coords.x)


new_grids: list[list[bool]] = []
for x in range(N):
    new_row: list[bool] = []
    for y in range(N):
        # ローテする回数は壁までの最小距離
        rotate_num = min(x + 1, y + 1, N - x, N - y)
        rotate_num %= 4
        original_coods = Coords(x, y)
        for _ in range(rotate_num):
            original_coods = before_coords(original_coods)
        new_grid = grids[original_coods.x][original_coods.y]
        new_row.append(new_grid)
    new_grids.append(new_row)

for i in range(N):
    answer_row: list[str] = []
    for j in range(N):
        if new_grids[i][j]:
            answer_row.append("#")
        else:
            answer_row.append(".")
    print("".join(answer_row))
