# AC
import sys
from collections import deque


class Node:
    def __init__(self, h: int, w: int) -> None:
        self.h = h
        self.w = w
        self.to_nodes: list[Node] = []
        self.direction: str | None = None
        self.is_wall = False
        self.is_start = False
        self.distance = sys.maxsize

    def __repr__(self) -> str:
        return str(self.direction)

    @property
    def show(self):
        if self.direction is None:
            raise
        return self.direction


H, W = map(int, input().split())

nodes: list[list[Node]] = []
start_nodes: list[Node] = []
for h in range(H):
    S = input()
    row: list[Node] = []
    for w, s in enumerate(S):
        node = Node(h, w)
        if s == "#":
            node.is_wall = True
            node.direction = s
        if s == "E":
            start_nodes.append(node)
            node.direction = s
            node.is_start = True
            node.distance = 0
        row.append(node)
    nodes.append(row)

d: deque[Node] = deque()
for start_node in start_nodes:
    d.append(start_node)
while d:
    node = d.popleft()
    if node.direction is None:
        raise

    dhs = [0, -1, 0, 1]
    dws = [1, 0, -1, 0]
    dirs = ["<", "v", ">", "^"]

    for i in range(4):
        dh = dhs[i]
        dw = dws[i]
        dir = dirs[i]

        to_h = node.h + dh
        to_w = node.w + dw
        if 0 <= to_h < H and 0 <= to_w < W:
            to_node = nodes[to_h][to_w]
            if (
                not to_node.is_wall
                and not to_node.is_start
                and to_node.distance > node.distance + 1
            ):
                to_node.direction = dir
                to_node.distance = node.distance + 1
                d.append(to_node)


for row in nodes:
    print("".join([node.show for node in row]))
