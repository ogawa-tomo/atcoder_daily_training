# TLE
from itertools import combinations

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

answer = -1
for a in combinations(A, K):
    s = sum(a)
    if s % D == 0:
        answer = max(answer, s)

print(answer)
