from collections import defaultdict
from itertools import combinations

N = int(input())

# px[y]: y座標がyにあるポイントのx座標のset
px: defaultdict[int, set[int]] = defaultdict(set)

for _ in range(N):
    x, y = map(int, input().split())
    px[y].add(x)

answer = 0
for y1 in px:
    x_set = px[y1]
    for x_pair in combinations(x_set, 2):
        x1 = x_pair[0]
        x2 = x_pair[1]
        for y2 in px:
            if y2 <= y1:
                continue
            x_set2 = px[y2]
            if x1 in x_set2 and x2 in x_set2:
                answer += 1

print(answer)
