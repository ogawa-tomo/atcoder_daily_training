from itertools import permutations


class Link:
    def __init__(self, n1: int, n2: int) -> None:
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
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    takahashi_links.add(Link(a, b))
aoki_links: set[Link] = set()
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    aoki_links.add(Link(c, d))

for aoki_balls in permutations(range(N)):
    new_aoki_links: set[Link] = set()
    for aoki_link in aoki_links:
        ball1 = aoki_balls[aoki_link.left]
        ball2 = aoki_balls[aoki_link.right]
        new_aoki_links.add(Link(ball1, ball2))
    # print(takahashi_links, new_aoki_links)
    if takahashi_links == new_aoki_links:
        print("Yes")
        exit()

print("No")
