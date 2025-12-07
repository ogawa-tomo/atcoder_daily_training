N = int(input())
S = list(map(int, input().split()))

A: list[int] = []
for i in range(N):
    s = S[i]
    if i == 0:
        A.append(s)
        continue
    prev_s = S[i - 1]
    A.append(s - prev_s)

print(*A)
