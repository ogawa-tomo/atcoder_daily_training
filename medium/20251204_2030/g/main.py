class CumulativeSum:
    def __init__(self, _list: list[int]):
        self._list = _list
        total = 0
        self.cumulative_sum_list: list[int] = []
        for elem in self._list:
            total += elem
            self.cumulative_sum_list.append(total)

    def sum(self, index: int):
        if index == -1:
            return 0
        return self.cumulative_sum_list[index]

    def range_sum(self, left_index: int, right_index: int):
        return self.sum(right_index) - self.sum(left_index - 1)


N = int(input())
X = list(map(int, input().split()))
P = list(map(int, input().split()))


class Village:
    def __init__(self, x: int, p: int):
        self.x = x
        self.p = p


villages: list[Village] = []
for i in range(N):
    villages.append(Village(X[i], P[i]))

cum_sum = CumulativeSum(P)
# cum_sum.range_sum(i, j): i番目の村からj番目の村までの人数

Q = int(input())
for _ in range(Q):
    l, r = map(int, input().split())

    # 座標がl以上であるような最小の村番号を求める
    ok = N
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if villages[mid].x >= l:
            ok = mid
        else:
            ng = mid
    left_index = ok
    if left_index == N:
        print(0)
        continue

    # 座標がr以下であるような最大の村番号を求める
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if villages[mid].x <= r:
            ok = mid
        else:
            ng = mid
    right_index = ok
    if right_index == -1:
        print(0)
        continue

    if left_index > right_index:
        print(0)
        continue

    print(cum_sum.range_sum(left_index, right_index))
