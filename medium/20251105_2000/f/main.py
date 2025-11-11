from collections import defaultdict

d: defaultdict[int, int] = defaultdict(int)
kinds = 0
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        d[x] += 1
        if d[x] == 1:
            kinds += 1
    elif query[0] == 2:
        x = query[1]
        d[x] -= 1
        if d[x] == 0:
            kinds -= 1
    elif query[0] == 3:
        print(kinds)
