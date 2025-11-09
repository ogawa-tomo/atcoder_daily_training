from collections import defaultdict
import heapq

d: defaultdict[int, int] = defaultdict(int)
max_list: list[int] = []
min_list: list[int] = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        d[x] += 1
        if d[x] == 1:
            heapq.heappush(max_list, -x)
            heapq.heappush(min_list, x)
    elif query[0] == 2:
        x = query[1]
        c = query[2]
        d[x] = max(d[x] - c, 0)
    elif query[0] == 3:
        while True:
            max_s = -max_list[0]
            if d[max_s] > 0:
                break
            else:
                heapq.heappop(max_list)
        while True:
            min_s = min_list[0]
            if d[min_s] > 0:
                break
            else:
                heapq.heappop(min_list)
        print(max_s - min_s)
