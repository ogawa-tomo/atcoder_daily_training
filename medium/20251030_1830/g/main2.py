# TLE
from itertools import permutations
import math

# print(math.factorial(8) * 16**2 * 8)
# print(len(list(permutations([0] * 16, 8))))

# print(16 * 15)

N = int(input())

A: list[list[int]] = []
for _ in range(2 * N - 1):
    A.append(list(map(int, input().split())))

# print(A)
people = list(range(2 * N))

answer = 0
for group1 in permutations(people, N):
    group2: list[int] = []
    for p in people:
        if p not in group1:
            group2.append(p)
    score = 0
    print(group1, group2)
    for k in range(N):
        # k番目のペアのスコア
        pair = (group1[k], group2[k])
        i = min(pair)
        j = max(pair)
        # print(pair, i, j)
        score ^= A[i][j - i - 1]
    answer = max(answer, score)

print(answer)
