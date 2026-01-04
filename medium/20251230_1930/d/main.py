N, A, B = map(int, input().split())

grids: list[list[str]] = []
for i in range(A * N):
    row: list[str] = []
    for j in range(B * N):
        if (i // A) % 2 == (j // B) % 2:
            row.append(".")
        else:
            row.append("#")
    grids.append(row)

for row in grids:
    print("".join(row))
