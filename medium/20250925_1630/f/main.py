import math

N = int(input())
max_r = 0
min_r = 10**9
max_c = 0
min_c = 10**9
for _ in range(N):
    r, c = map(int, input().split())
    max_r = max(max_r, r)
    min_r = min(min_r, r)
    max_c = max(max_c, c)
    min_c = min(min_c, c)

print(max(math.ceil((max_r - min_r) / 2), math.ceil((max_c - min_c) / 2)))
