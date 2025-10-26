import heapq

q: list[int] = []
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        heapq.heappush(q, x)
    else:
        x = heapq.heappop(q)
        print(x)
