import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self) -> None:
        self.parent: Node | None = None
        self.size = 1

    def root(self):
        if self.parent is None:
            return self
        return self.parent.root()

    def root_size(self):
        return self.root().size


def is_same(node1: Node, node2: Node):
    return node1.root() == node2.root()


def unite(node1: Node, node2: Node):
    root1 = node1.root()
    root2 = node2.root()
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


class Edge:
    def __init__(self, weight: int, from_node: Node, to_node: Node):
        self.weight = weight
        self.from_node = from_node
        self.to_node = to_node

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return str(self.weight)


N = int(input())
nodes = [Node() for _ in range(N)]
edges: list[Edge] = []

for _ in range(N - 1):
    u, v, w = map(int, input().split())
    node_u = nodes[u - 1]
    node_v = nodes[v - 1]
    edges.append(Edge(w, node_u, node_v))

edges.sort()
# print(edges)
answer = 0
for edge in edges:
    from_node = edge.from_node
    to_node = edge.to_node
    answer += edge.weight * from_node.root_size() * to_node.root_size()
    unite(from_node, to_node)
print(answer)
