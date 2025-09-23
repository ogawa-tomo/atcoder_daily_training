from collections import deque

N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.visited = False
        self.distance = -1


nodes = [Node() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].neighbors.append(nodes[b])


d: deque[Node] = deque()
d.append(nodes[0])
nodes[0].distance = 0

while d:
    node = d.popleft()
    distance = node.distance
    for neighbor in node.neighbors:
        if neighbor == nodes[0]:
            print(distance + 1)
            exit()
        if neighbor.distance == -1:
            d.append(neighbor)
            neighbor.distance = distance + 1

print(-1)
