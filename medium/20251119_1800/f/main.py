from collections import deque

N = int(input())
H_ = list(map(int, input().split()))
H: deque[int] = deque()
for h in H_:
    H.append(h)

T = 0
while H:
    h = H.popleft()

    # 前準備
    if T > 0:
        T += 1
        if T % 3 != 0:
            h -= 1
        else:
            h -= 3
        if h <= 0:
            continue

    # Tが3の倍数になるまで調整
    if T % 3 == 1:
        T += 1
        h -= 1
        if h <= 0:
            continue
    if T % 3 == 2:
        T += 1
        h -= 3
        if h <= 0:
            continue

    # Tが3増えるごとに5減るので、その繰り返しの数
    # 繰り返した結果hが-2になることもあることを考慮すると、繰り返しの数はこうなる
    three_turns = (h + 2) // 5
    T += three_turns * 3
    h -= three_turns * 5

    # この時点で負ならおわり
    if h <= 0:
        continue

    # 0以下になるまで最大あと2回繰り返す
    T += 1
    h -= 1
    if h <= 0:
        continue
    T += 1
    h -= 1
    if h <= 0:
        continue

print(T)
