from collections import deque


class Grid:
    def __init__(self, s: str) -> None:
        self.s = s
        self.distance: int | None = None
        self.to_grids: list[Grid] = []

    @property
    def is_safety(self):
        return self.s == "."

    def __repr__(self) -> str:
        return self.s


# 多始点BFS
def bfs(start_nodes: list[Grid], K: int):
    answer = 0
    d: deque[Grid] = deque()

    for node in start_nodes:
        d.append(node)
        node.distance = 0
        answer += 1
    while d:
        node = d.popleft()
        if node.distance is None:
            raise
        distance = node.distance
        to_distance = distance + 1
        if to_distance > K:
            break
        for to_node in node.to_grids:
            if to_node.distance is None:
                d.append(to_node)
                to_node.distance = to_distance
                answer += 1
    return answer


H, W, K = map(int, input().split())

grids: list[list[Grid]] = []
for _ in range(H):
    S = input()
    row: list[Grid] = []
    for s in S:
        grid = Grid(s)
        row.append(grid)
    grids.append(row)

# print(grids)

for h in range(H):
    for w in range(W):
        grid = grids[h][w]
        if not grid.is_safety:
            continue
        dhs = [1, 0, -1, 0]
        dws = [0, 1, 0, -1]
        for i in range(4):
            hh = h + dhs[i]
            ww = w + dws[i]
            if 0 <= hh < H and 0 <= ww < W:
                neighbor = grids[hh][ww]
                if neighbor.is_safety:
                    grid.to_grids.append(neighbor)


safety_rows: list[int] = []
safety_columns: list[int] = []
for h in range(H):
    safety = True
    for w in range(W):
        grid = grids[h][w]
        if not grid.is_safety:
            safety = False
            break
    if safety:
        safety_rows.append(h)

for w in range(W):
    safety = True
    for h in range(H):
        grid = grids[h][w]
        if not grid.is_safety:
            safety = False
            break
    if safety:
        safety_columns.append(w)

safety_grids: list[Grid] = []
for h in safety_rows:
    for w in safety_columns:
        grid = grids[h][w]
        safety_grids.append(grid)

answer = bfs(safety_grids, K)
print(answer)
