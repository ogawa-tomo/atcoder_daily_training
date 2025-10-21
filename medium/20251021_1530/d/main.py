H, W = map(int, input().split())

grids: list[list[int]] = []

for i in range(H):
    row = list(map(int, input().split()))
    grids.append(row)

# print(grids)
for i1 in range(H - 1):
    for j1 in range(W - 1):
        for i2 in range(i1 + 1, H):
            for j2 in range(j1 + 1, W):
                if grids[i1][j1] + grids[i2][j2] > grids[i2][j1] + grids[i1][j2]:
                    print("No")
                    exit()

print("Yes")
