from itertools import permutations


class Link:
    def __init__(self, n1: int, n2: int) -> None:
        self.left = min(n1, n2)
        self.right = max(n1, n2)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Link):
            raise
        return self.left == other.left and self.right == other.right


N, M = map(int, input().split())

takahashi_links: set[tuple[int, int]] = set()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    takahashi_links.add((a, b))
aoki_links: set[tuple[int, int]] = set()
for _ in range(M):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    aoki_links.add((c, d))

for aoki_balls in permutations(range(N)):
    new_aoki_links: set[tuple[int, int]] = set()
    for aoki_link in aoki_links:
        ball1 = aoki_balls[aoki_link[0]]
        ball2 = aoki_balls[aoki_link[1]]
        new_aoki_links.add((min(ball1, ball2), max(ball1, ball2)))

    if takahashi_links == new_aoki_links:
        print("Yes")
        exit()

print("No")
