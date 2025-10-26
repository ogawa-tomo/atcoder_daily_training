N = 8

grids: list[list[str]] = []
for i in range(N):
    row = list(input())
    grids.append(row)

# print(grids)
rook_i_set: set[int] = set()
rook_j_set: set[int] = set()
for i in range(N):
    for j in range(N):
        if grids[i][j] == "#":
            rook_i_set.add(i)
            rook_j_set.add(j)

# print(rook_i_set)
# print(rook_j_set)
answer = 0
for i in range(N):
    for j in range(N):
        if i not in rook_i_set and j not in rook_j_set:
            answer += 1

print(answer)
