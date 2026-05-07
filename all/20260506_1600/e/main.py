import heapq
from collections import defaultdict

Q = int(input())
d: defaultdict[int, int] = defaultdict(int)
min_q: list[int] = []
max_q: list[int] = []  # 負の値を入れる
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x = q[1]
        d[x] += 1
        heapq.heappush(min_q, x)
        heapq.heappush(max_q, -x)
    elif q[0] == 2:
        x = q[1]
        c = q[2]
        d[x] = max(0, d[x] - c)
    elif q[0] == 3:
        while True:
            if d[min_q[0]] > 0:
                min_value = min_q[0]
                break
            else:
                heapq.heappop(min_q)
        while True:
            if d[-max_q[0]] > 0:
                max_value = -max_q[0]
                break
            else:
                heapq.heappop(max_q)
        print(max_value - min_value)
