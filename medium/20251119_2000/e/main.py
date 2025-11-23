from collections import deque

N, M = map(int, input().split())


class Node:
    def __init__(self) -> None:
        self.to_nodes: list[Node] = []
        self.investigated = False


nodes = [Node() for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].to_nodes.append(nodes[v])
    nodes[v].to_nodes.append(nodes[u])


connected_component_num = 0
for start_node in nodes:
    if start_node.investigated:
        continue
    connected_component_num += 1
    d: deque[Node] = deque()
    start_node.investigated = True
    d.append(start_node)
    while d:
        node = d.popleft()
        for to_node in node.to_nodes:
            if not to_node.investigated:
                to_node.investigated = True
                d.append(to_node)

print(connected_component_num)
