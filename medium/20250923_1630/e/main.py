N, K = map(int, input().split())
mod = 10**9

A: list[int] = []
prev = 0
for i in range(N + 1):
    if i < K:
        A.append(1)
        prev += 1
        continue
    A.append(prev)
    prev = (2 * prev) % mod
    prev = (prev - A[i - K]) % mod

print(A[N])
