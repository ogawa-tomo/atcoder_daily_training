import heapq
import sys

max_distance = sys.maxsize


class Node:
    def __init__(self, strength: int) -> None:
        self.strength = strength
        self.to_nodes: list[Node] = []
        self.added_to_queue = False

    def __repr__(self):
        return str(self.strength)

    def __lt__(self, other):
        return self.strength < other.strength


H, W, X = map(int, input().split())
P, Q = map(int, input().split())

nodes: list[list[Node]] = []
for h in range(H):
    S = list(map(int, input().split()))
    row: list[Node] = []
    for s in S:
        node = Node(s)
        row.append(node)
    nodes.append(row)

for h in range(H):
    for w in range(W):
        node = nodes[h][w]
        if h > 0:
            node.to_nodes.append(nodes[h - 1][w])
        if h < H - 1:
            node.to_nodes.append(nodes[h + 1][w])
        if w > 0:
            node.to_nodes.append(nodes[h][w - 1])
        if w < W - 1:
            node.to_nodes.append(nodes[h][w + 1])

start_node = nodes[P - 1][Q - 1]
start_node.added_to_queue = True
total_strength = start_node.strength
q: list[Node] = []
for to_node in start_node.to_nodes:
    heapq.heappush(q, to_node)
    to_node.added_to_queue = True
while q:
    node = heapq.heappop(q)

    if node.strength * X >= total_strength:
        break
    total_strength += node.strength
    for to_node in node.to_nodes:
        if not to_node.added_to_queue:
            heapq.heappush(q, to_node)
            to_node.added_to_queue = True

print(total_strength)
