from collections import deque


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.distance = -1  # 頂点0またはN1+N2-1からの距離


N1, N2, M = map(int, input().split())
nodes: list[Node] = []
for _ in range(N1 + N2):
    nodes.append(Node())

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])
    nodes[b].neighbors.append(nodes[a])


def max_distance(start_node: Node):
    d: deque[Node] = deque()
    max_1 = 0
    d.append(start_node)
    start_node.distance = 0
    while d:
        node = d.popleft()
        distance = node.distance
        for neighbor in node.neighbors:
            if neighbor.distance == -1:
                d.append(neighbor)
                neighbor.distance = distance + 1
                max_1 = max(max_1, neighbor.distance)
    return max_1


max_1 = max_distance(nodes[0])
max_2 = max_distance(nodes[N1 + N2 - 1])

print(max_1 + max_2 + 1)
