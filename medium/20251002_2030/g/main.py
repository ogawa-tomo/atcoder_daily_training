from itertools import permutations

N, H, W = map(int, input().split())


class Tile:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b
        self.reverse = False

    def width(self):
        if not self.reverse:
            return self.a
        else:
            return self.b

    def height(self):
        if not self.reverse:
            return self.b
        else:
            return self.a


class Grid:
    def __init__(self):
        self.covered = False

    def __repr__(self):
        if self.covered:
            return "#"
        else:
            return "."


grids: list[list[Grid]] = []
for h in range(H):
    row = [Grid() for _ in range(W)]
    grids.append(row)


def reset_grids():
    for h in range(H):
        for w in range(W):
            grids[h][w].covered = False


def most_left_upper_uncevored_grid_position():
    for h in range(H):
        for w in range(W):
            if not grids[h][w].covered:
                return [h, w]
    return None


def put_tile(tile: Tile):
    p = most_left_upper_uncevored_grid_position()
    if p is None:
        return False
    start_h = p[0]
    start_w = p[1]
    if start_h + tile.height() > H or start_w + tile.width() > W:
        return False
    for h in range(start_h, start_h + tile.height()):
        for w in range(start_w, start_w + tile.width()):
            grid = grids[h][w]
            if grid.covered:
                return False
            grid.covered = True
    return True


def all_covered():
    for h in range(H):
        for w in range(W):
            if not grids[h][w].covered:
                return False
    return True


tiles: list[Tile] = []

for _ in range(N):
    a, b = map(int, input().split())
    tile = Tile(a, b)
    tiles.append(tile)


for tile_select_pattern in permutations(tiles):
    # それぞれのタイルを表向きにするか、裏向きにするかの2**N通り
    for i in range(1 << N):
        reset_grids()

        for j, tile in enumerate(tile_select_pattern):
            if i >> j & 1:
                tile.reverse = True
            else:
                tile.reverse = False

        # 左上から順番に敷き詰めていく
        for tile in tile_select_pattern:
            result = put_tile(tile)
            if not result:
                break
            if all_covered():
                print("Yes")
                exit()
print("No")
