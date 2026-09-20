# TLE
from collections import deque


class Node:
    def __init__(self, height: int) -> None:
        self.height = height
        self.to_links: list[Link] = []
        self.max_joy: int | None = None  # ここにたどり着くときの嬉しさの最大値


class Link:
    def __init__(self, to_node: Node, joy_diff: int) -> None:
        self.to_node = to_node
        self.joy_diff = joy_diff


def bfs(start_node: Node):
    d: deque[Node] = deque()

    d.append(start_node)
    start_node.max_joy = 0
    while d:
        node = d.popleft()
        if node.max_joy is None:
            raise
        for to_link in node.to_links:
            to_node = to_link.to_node
            if (
                to_node.max_joy is None
                or to_node.max_joy < node.max_joy + to_link.joy_diff
            ):
                d.append(to_node)
                to_node.max_joy = node.max_joy + to_link.joy_diff


N, M = map(int, input().split())


nodes: list[Node] = []
H = list(map(int, input().split()))
for h in H:
    nodes.append(Node(h))

for _ in range(M):
    u, v = map(int, input().split())
    node_u = nodes[u - 1]
    node_v = nodes[v - 1]
    if node_u.height > node_v.height:
        node_u.to_links.append(Link(node_v, node_u.height - node_v.height))
        node_v.to_links.append(Link(node_u, -2 * (node_u.height - node_v.height)))
    else:
        node_u.to_links.append(Link(node_v, -2 * (node_v.height - node_u.height)))
        node_v.to_links.append(Link(node_u, node_v.height - node_u.height))

bfs(nodes[0])
answer = 0
for node in nodes:
    if node.max_joy is None:
        raise
    answer = max(answer, node.max_joy)
print(answer)
