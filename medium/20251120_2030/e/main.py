import sys

N, M = map(int, input().split())


class Node:
    def __init__(self, i: int):
        self.i = i
        self.is_black = True


class Edge:
    def __init__(self, from_node: Node, to_node: Node):
        self.from_node = from_node
        self.to_node = to_node


nodes = [Node(i) for i in range(N)]
edges: list[Edge] = []
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    edge = Edge(node_u, node_v)
    edges.append(edge)

answer = sys.maxsize
for k in range(1 << N):
    for i in range(N):
        node = nodes[i]
        node.is_black = bool(k & (1 << i))
    tmp_answer = 0
    for edge in edges:
        if edge.from_node.is_black == edge.to_node.is_black:
            tmp_answer += 1
    answer = min(answer, tmp_answer)

print(answer)
