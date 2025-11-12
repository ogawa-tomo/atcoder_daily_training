import sys
from collections import deque


class Node:
    def __init__(self) -> None:
        self.to_nodes: list[Node] = []
        self.investigated = False


N, M = map(int, input().split())

nodes = [Node() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)

connected_count = 0
for root_node in nodes:
    if root_node.investigated:
        continue
    connected_count += 1
    d: deque[Node] = deque()
    d.append(root_node)
    while d:
        node = d.popleft()
        node.investigated = True
        for to_node in node.to_nodes:
            if not to_node.investigated:
                d.append(to_node)

print(M - (N - connected_count))
