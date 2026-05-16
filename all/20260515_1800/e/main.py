N, M = map(int, input().split())
occupied: set[tuple[int, int]] = set()
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    occupied.add((a, b))

    dxs = [2, 1, -1, -2, -2, -1, 1, 2]
    dys = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        dx = dxs[i]
        dy = dys[i]
        aa = a + dx
        bb = b + dy
        if 0 <= aa and aa <= N - 1 and 0 <= bb and bb <= N - 1:
            occupied.add((aa, bb))

print(N**2 - len(occupied))
