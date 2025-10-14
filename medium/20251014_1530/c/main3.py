# AC
from collections import defaultdict

N, S = map(int, input().split())
A = list(map(int, input().split()))

d: defaultdict[int, int] = defaultdict(int)

answer = 0
for a in A:
    target = S - a
    answer += d[target]
    d[a] += 1

print(answer)
