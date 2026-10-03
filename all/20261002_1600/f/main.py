N = int(input())
P = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    right = P[i]
    left = P[i - 1]

    if left > right:
        new_left_candids = set(P[i:])
        new_left = 0
        for candid in new_left_candids:
            if candid < left:
                new_left = max(new_left, candid)
        new_left_candids.remove(new_left)
        new_left_candids.add(left)
        nokori = list(new_left_candids)
        nokori.sort(reverse=True)
        answer = P[: i - 1]
        answer.append(new_left)
        answer.extend(nokori)
        print(*answer)
        exit()
