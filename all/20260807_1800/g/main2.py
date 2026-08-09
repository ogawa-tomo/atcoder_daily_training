from collections import deque


class Node:
    def __init__(self) -> None:
        self.x: int | None = None
        self.to_edges: list[Edge] = []
        self.from_edges: list[Edge] = []


class Edge:
    def __init__(self, from_node: Node, to_node: Node, weight: int) -> None:
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight


N, M = map(int, input().split())
nodes = [Node() for _ in range(N)]
edges: list[Edge] = []
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    from_node = nodes[u]
    to_node = nodes[v]
    edge = Edge(from_node, to_node, w)
    edges.append(edge)
    from_node.to_edges.append(edge)
    to_node.from_edges.append(edge)


for node in nodes:
    if node.x is not None:
        continue
    d: deque[Node] = deque()
    d.append(node)
    node.x = 0
    while d:
        current_node = d.popleft()
        if current_node.x is None:
            raise
        for to_edge in current_node.to_edges:
            to_node = to_edge.to_node
            if to_node.x is None:
                to_node.x = current_node.x + to_edge.weight
                d.append(to_node)
        for from_edge in current_node.from_edges:
            from_node = from_edge.from_node
            if from_node.x is None:
                from_node.x = current_node.x - from_edge.weight
                d.append(from_node)

print(*[node.x for node in nodes])
