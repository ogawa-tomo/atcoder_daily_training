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


N, M = map(int, input().split())
S = list(input())
T = list(input())

covers: list[Cover] = []
for _ in range(M):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    cover = Cover(l, r)
    covers.append(cover)

# swapped[i]: i番目の文字が何回入れ替わったか
swapped = Coverd1D(covers, N).coverd

answer: list[str] = []
for i in range(N):
    swapped_num = swapped[i]
    if swapped_num % 2 == 0:
        answer.append(S[i])
    else:
        answer.append(T[i])

print("".join(answer))
