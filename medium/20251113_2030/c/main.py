N = int(input())

A: list[list[int]] = []
A.append([1])
for i in range(1, N):
    Ai: list[int] = []
    for j in range(i + 1):
        if j == 0 or j == i:
            Ai.append(1)
        else:
            Ai.append(A[i - 1][j - 1] + A[i - 1][j])
    A.append(Ai)

for a in A:
    print(*a)
