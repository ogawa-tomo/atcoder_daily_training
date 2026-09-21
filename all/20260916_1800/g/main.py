# TLE
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

for start_node in start_nodes:
    d: deque[Node] = deque()
    d.append(start_node)
    start_node.direction = "E"
    while d:
        node = d.popleft()
        if node.direction is None:
            raise
        # distance = node.distance

        # 上
        if node.h > 0:
            upper_node = nodes[node.h - 1][node.w]
            if (
                not upper_node.is_wall
                and not upper_node.is_start
                and upper_node.distance > node.distance + 1
                # and upper_node.direction != "v"
            ):
                upper_node.direction = "v"
                upper_node.distance = node.distance + 1
                d.append(upper_node)
        # 下
        if node.h < H - 1:
            below_node = nodes[node.h + 1][node.w]
            if (
                not below_node.is_wall
                and not below_node.is_start
                and below_node.distance > node.distance + 1
                # and below_node.direction != "^"
            ):
                below_node.direction = "^"
                below_node.distance = node.distance + 1
                d.append(below_node)
        # 左
        if node.w > 0:
            left_node = nodes[node.h][node.w - 1]
            if (
                not left_node.is_wall
                and not left_node.is_start
                and left_node.distance > node.distance + 1
                # and left_node.direction != ">"
            ):
                left_node.direction = ">"
                left_node.distance = node.distance + 1
                d.append(left_node)

        # 右
        if node.w < W - 1:
            right_node = nodes[node.h][node.w + 1]
            if (
                not right_node.is_wall
                and not right_node.is_start
                and right_node.distance > node.distance + 1
                # and right_node.direction != "<"
            ):
                right_node.direction = "<"
                right_node.distance = node.distance + 1
                d.append(right_node)

for row in nodes:
    print("".join([node.show for node in row]))
