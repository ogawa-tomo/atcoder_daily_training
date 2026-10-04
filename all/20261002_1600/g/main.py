class Link:
    def __init__(self, n1: int, n2: int) -> None:
        if n1 == n2:
            raise
        self.n1 = min(n1, n2)
        self.n2 = max(n1, n2)

    @property
    def node_set(self):
        return {self.n1, self.n2}

    def includes(self, n: int):
        return n in self.node_set

    def another_one(self, n: int):
        if self.n1 == n:
            return self.n2
        elif self.n2 == n:
            return self.n1
        raise

    def __eq__(self, other):
        if not isinstance(other, Link):
            raise
        return self.n1 == other.n1 and self.n2 == other.n2

    def __hash__(self) -> int:
        return hash((self.n1, self.n2))

    def __lt__(self, other):
        if not isinstance(other, Link):
            raise
        if self.n1 == other.n1:
            return self.n2 < other.n2
        return self.n1 < other.n1

    def __repr__(self) -> str:
        return str(self.node_set)


N, M = map(int, input().split())

links: list[Link] = []
for _ in range(M):
    a, b = map(int, input().split())
    link = Link(a, b)
    links.append(link)

links = list(set(links))
links.sort()
# print(links)

answers: set[Link] = set()

n1 = links[0].n1
n2 = links[0].n2
for node in [n1, n2]:
    not_include_node_links: set[Link] = set()
    for link in links:
        if not link.includes(node):
            not_include_node_links.add(link)

    if len(not_include_node_links) == 0:
        for another in range(1, N + 1):
            if another == node:
                continue
            link = Link(node, another)
            answers.add(link)
    else:
        another_node_set = list(not_include_node_links)[0].node_set
        for link in not_include_node_links:
            another_node_set &= link.node_set
        for another_node in another_node_set:
            link = Link(node, another_node)
            answers.add(link)

print(len(answers))
