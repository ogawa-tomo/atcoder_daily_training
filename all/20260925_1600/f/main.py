N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

A -= 1
B -= 1
P -= 1
Q -= 1
R -= 1
S -= 1

grids: list[list[str]] = []
for i in range(P, Q + 1):
    row: list[str] = []
    for j in range(R, S + 1):
        if abs(i - A) == abs(j - B):
            row.append("#")
        else:
            row.append(".")
    grids.append(row)

for row in grids:
    print("".join(row))
