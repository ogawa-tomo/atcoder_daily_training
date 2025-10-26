from collections import deque

N = int(input())
S = list(input())

answer: deque[int] = deque()
answer.append(N)
for i in range(N):
    d = S[N - i - 1]
    n = N - i - 1
    if d == "L":
        answer.append(n)
    else:
        answer.appendleft(n)

print(" ".join([str(a) for a in answer]))
