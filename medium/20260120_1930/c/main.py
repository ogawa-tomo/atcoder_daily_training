S: list[list[str]] = []
for _ in range(10):
    S.append(list(input()))

# print(S)
A = 10
B = 0
C = 10
D = 0
for i in range(10):
    for j in range(10):
        s = S[i][j]
        if s == "#":
            A = min(A, i + 1)
            B = max(B, i + 1)
            C = min(C, j + 1)
            D = max(D, j + 1)

print(A, B)
print(C, D)
