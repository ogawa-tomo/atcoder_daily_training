from itertools import permutations


class Node:
    def __init__(self, i: int) -> None:
        self.i = i

    def __lt__(self, other):
        if not isinstance(other, Node):
            raise
        return self.i < other.i

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            raise
        return self.i == other.i

    def __hash__(self) -> int:
        return self.i

    def __repr__(self) -> str:
        return str(self.i)


class Link:
    def __init__(self, n1: Node, n2: Node) -> None:
        self.left = min(n1, n2)
        self.right = max(n1, n2)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Link):
            raise
        return self.left == other.left and self.right == other.right

    def __hash__(self) -> int:
        return hash((self.left, self.right))

    def __repr__(self) -> str:
        return str((self.left, self.right))


N, M = map(int, input().split())

takahashi_links: set[Link] = set()
takahashi_nodes = [Node(i) for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node_a = takahashi_nodes[a]
    node_b = takahashi_nodes[b]
    takahashi_links.add(Link(node_a, node_b))
aoki_links: set[Link] = set()
aoki_nodes = [Node(i) for i in range(N)]
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    node_c = aoki_nodes[c]
    node_d = aoki_nodes[d]
    aoki_links.add(Link(node_c, node_d))

for new_aoki_nodes in permutations(aoki_nodes):
    new_aoki_links: set[Link] = set()
    for aoki_link in aoki_links:
        ball1 = new_aoki_nodes[aoki_link.left.i]
        ball2 = new_aoki_nodes[aoki_link.right.i]
        new_aoki_links.add(Link(ball1, ball2))
    # print(takahashi_links, new_aoki_links)
    if takahashi_links == new_aoki_links:
        print("Yes")
        exit()

print("No")
