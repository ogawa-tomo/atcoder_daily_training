from collections import deque

d: deque[int] = deque()
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        d.append(x)
    elif q[0] == 2:
        print(d.popleft())
