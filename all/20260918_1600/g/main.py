# ぜんぜんだめ。累積和の問題ではない
class Cover:
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


class Coverd1D:
    def __init__(self, covers: list[Cover], length: int):
        # 出席者数の前日比
        x = [0] * (length + 1)
        for cover in covers:
            x[cover.left] += 1
            x[cover.right + 1] -= 1

        # 累積和
        self.coverd: list[int] = []
        total = 0
        for i in range(length):
            total += x[i]
            self.coverd.append(total)


N = int(input())

# 登場した数のリスト
nums: list[int] = []

covers: list[Cover] = []
for _ in range(N):
    l, r = map(int, input().split())
    nums.append(l)
    nums.append(r)
    covers.append(Cover(l, r))

nums.sort()

# d[n]: 数に対応するインデックス
d: dict[int, int] = {}
for i, n in enumerate(nums):
    d[n] = i

covers2: list[Cover] = []
for cover in covers:
    l = cover.left
    r = cover.right
    cover2 = Cover(d[l], d[r])
    covers2.append(cover2)

length = nums[-1] + 1
coverd = Coverd1D(covers2, length).coverd
answer = 0
for cover2 in covers2:
    answer += max(coverd[cover2.left : cover2.right + 1]) - 1
print(answer)
