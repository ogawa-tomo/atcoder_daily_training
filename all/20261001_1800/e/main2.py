N, Q = map(int, input().split())
A = list(map(int, input().split()))

# d[x]: xが出てきたインデックスを格納するリスト
d: dict[int, list[int]] = {}
for i in range(N):
    a = A[i]
    if a not in d:
        d[a] = []
    d[a].append(i + 1)


for _ in range(Q):
    x, k = map(int, input().split())
    k -= 1
    if x in d and len(d[x]) > k:
        print(d[x][k])
    else:
        print(-1)
