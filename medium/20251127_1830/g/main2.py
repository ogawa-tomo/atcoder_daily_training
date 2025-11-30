from collections import deque

S = list(input())
K = int(input())

q: deque[str] = deque()
k = 0
answer = 0
for s in S:
    q.append(s)
    if s == ".":
        k += 1

    while k > K:
        drop = q.popleft()
        if drop == ".":
            k -= 1

    answer = max(answer, len(q))

print(answer)
