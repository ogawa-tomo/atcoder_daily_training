X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

parts: set[int] = set()
for _ in range(Q):
    p = int(input())
    p -= 1
    if p in parts:
        parts.remove(p)
        X -= W[p]
    else:
        parts.add(p)
        X += W[p]
    print(X)
