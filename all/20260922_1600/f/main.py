class Cover:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


class Covered1D:
    def __init__(self, covers: list[Cover], length: int):
        # 出席者数の前日比
        x = [0] * (length + 1)
        for cover in covers:
            x[cover.left] += 1
            x[cover.right + 1] -= 1

        # 累積和
        self.covered: list[int] = []
        total = 0
        for i in range(length):
            total += x[i]
            self.covered.append(total)


N, M = map(int, input().split())

covers: list[Cover] = []
for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    cover = Cover(l, r)
    covers.append(cover)

covered = Covered1D(covers, N)
# print(covered.covered)
print(min(covered.covered))
