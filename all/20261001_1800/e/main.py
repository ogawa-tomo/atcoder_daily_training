from collections import defaultdict


N, Q = map(int, input().split())
A = list(map(int, input().split()))

# d[x][k]: xがk回目に出てくるインデックス
d: dict[int, dict[int, int]] = {}
# num[x]: xが出た回数
num: defaultdict[int, int] = defaultdict(int)
for i in range(N):
    a = A[i]
    num[a] += 1
    k = num[a]
    if a not in d:
        d[a] = {}
    d[a][k] = i + 1


for _ in range(Q):
    x, k = map(int, input().split())
    if x in d and k in d[x]:
        print(d[x][k])
    else:
        print(-1)
