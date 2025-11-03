# TLE
from itertools import combinations, permutations
import math

print(math.factorial(8) * 16**2 * 8)

N = int(input())

A: list[list[int]] = []
for _ in range(2 * N - 1):
    A.append(list(map(int, input().split())))

# print(A)
people = list(range(2 * N))

answer = 0
for group1 in combinations(people, N):
    # print(group1)
    group2: list[int] = []
    for p in people:
        if p not in group1:
            group2.append(p)
    # print("group")
    # print(group1, group2)

    # group1とgroup2をマッチングさせるN!通り
    for group1_perm in permutations(group1):
        score = 0
        # print(group1_perm)
        for k in range(N):
            # k番目のペアのスコア
            pair = (group1_perm[k], group2[k])
            i = min(pair)
            j = max(pair)
            # print(pair, i, j)
            score ^= A[i][j - i - 1]
        answer = max(answer, score)

print(answer)
