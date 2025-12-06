# MLE
N = int(input())


# クラス作ったからMLEになったのか？たまったもんじゃないぜ…
class Grid:
    def __init__(self, black: bool):
        self.black = black

    def __repr__(self):
        if self.black:
            return "#"
        else:
            return "."


grids: list[list[Grid]] = []
for _ in range(N):
    A = list(input())
    row: list[Grid] = []
    for a in A:
        row.append(Grid(a == "#"))
    grids.append(row)


# ローテする前のx, y
def before_xy(x: int, y: int):
    return (N - 1 - y, x)


# print(grids)
# new_grids = copy.deepcopy(grids)
new_grids: list[list[Grid]] = []
# for _ in range(N):
#     new_grids.append([Grid(True) for _ in range(N)])
for x in range(N):
    new_row: list[Grid] = []
    for y in range(N):
        rotate_num = min(x + 1, y + 1, N - x, N - y)
        rotate_num %= 4
        original_coods = (x, y)
        for _ in range(rotate_num):
            original_coods = before_xy(original_coods[0], original_coods[1])
        original_x = original_coods[0]
        original_y = original_coods[1]
        # new_grids[x][y] = grids[original_x][original_y]
        new_grid = Grid(grids[original_x][original_y].black)
        new_row.append(new_grid)
    new_grids.append(new_row)

for i in range(N):
    print("".join([str(grid) for grid in new_grids[i]]))
