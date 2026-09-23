N, K = map(int, input().split())
A = list(map(int, input().split()))

remA: list[int] = []
for a in A:
    remA.append(a % K)

remA.sort()

max_gap = 0
for i in range(N - 1):
    max_gap = max(max_gap, remA[i + 1] - remA[i])
max_gap = max(max_gap, remA[0] + (K - remA[N - 1]))

print(K - max_gap)
