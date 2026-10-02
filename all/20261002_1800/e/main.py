from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

# d[i]: クラスiの人数
d: defaultdict[int, int] = defaultdict(int)
for a in A:
    d[a] += 1

# print(d)
# print(max(d.values()))
max_class = max(d.values())

answer = 0
for i in range(1, K + 1):
    if d[i] >= max_class - 1:
        answer += 1

print(answer)
