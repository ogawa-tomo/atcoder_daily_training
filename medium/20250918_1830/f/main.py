N = int(input())

S: list[list[int]] = []
S.append([1])

for i in range(1, N):
    s = [*S[i - 1], i + 1, *S[i - 1]]
    S.append(s)

print(" ".join([str(s) for s in S[N - 1]]))
