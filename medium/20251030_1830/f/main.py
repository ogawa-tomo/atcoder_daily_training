N, M = map(int, input().split())
occupied: set[tuple[int, ...]] = set()
for _ in range(M):
    a, b = map(int, input().split())
    occupied.add((a, b))

    v_list = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
    for v in v_list:
        vi = v[0]
        vj = v[1]
        i = a + vi
        j = b + vj
        if 1 <= i and i <= N and 1 <= j and j <= N:
            occupied.add((i, j))

# print(occupied)
print(N**2 - len(occupied))
