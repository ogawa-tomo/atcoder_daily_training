import sys
from itertools import permutations


class Node:
    def __init__(self, i: int) -> None:
        self.i = i

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise
        return self.i < other.i

    def __eq__(self, other):
        if not isinstance(other, Node):
            raise
        return self.i == other.i

    def __hash__(self) -> int:
        return self.i


class Link:
    def __init__(self, node1: Node, node2: Node) -> None:
        self.node1 = min(node1, node2)
        self.node2 = max(node1, node2)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Link):
            raise
        return self.node1 == other.node1 and self.node2 == other.node2

    def __hash__(self) -> int:
        return hash((self.node1, self.node2))


N = int(input())
Mg = int(input())
g_nodes = [Node(i) for i in range(N)]
g_links: set[Link] = set()
for _ in range(Mg):
    u, v = map(int, input().split())
    node1 = g_nodes[u - 1]
    node2 = g_nodes[v - 1]
    g_links.add(Link(node1, node2))

Mh = int(input())
h_nodes = [Node(i) for i in range(N)]
h_links: set[Link] = set()
for _ in range(Mh):
    a, b = map(int, input().split())
    node1 = h_nodes[a - 1]
    node2 = h_nodes[b - 1]
    h_links.add(Link(node1, node2))
A: list[list[int]] = []
for i in range(N - 1):
    a = list(map(int, input().split()))
    row = [0] * (i + 1)
    row.extend(a)
    A.append(row)


def link_cost(link: Link):
    return A[link.node1.i][link.node2.i]


answer = sys.maxsize
for new_g_nodes in permutations(g_nodes):
    new_g_links: set[Link] = set()
    for g_link in g_links:
        node1 = new_g_nodes[g_link.node1.i]
        node2 = new_g_nodes[g_link.node2.i]
        new_g_links.add(Link(node1, node2))

    cost = 0
    for h_link in h_links:
        if h_link not in new_g_links:
            cost += link_cost(h_link)

    for new_g_link in new_g_links:
        if new_g_link not in h_links:
            cost += link_cost(new_g_link)

    answer = min(answer, cost)

print(answer)
