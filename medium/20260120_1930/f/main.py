from collections import defaultdict
import math

S = input()
N = len(S)
# print(N)

# 文字の出現回数をカウントするディクショナリ
d: defaultdict[str, int] = defaultdict(int)
for s in S:
    d[s] += 1

# 重複した数
duplicated = 0
for k in d:
    if d[k] > 1:
        duplicated += math.comb(d[k], 2)
if duplicated > 0:
    duplicated -= 1
print((N * (N - 1) // 2) - duplicated)
