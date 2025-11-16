a, b, C = map(int, input().split())


def popcount(i: int):
    return format(i, "b").count("1")


bin_C = format(C, "b")

one_count = popcount(C)

# one_count + 2k = a + b となるkが存在するか？
# k: Cが0のときに両方とも1にする回数
k = (a + b - one_count) / 2
if not k.is_integer() or k < 0:
    print(-1)
    exit()

k = int(k)
X: list[str] = []  # 1がa個
Y: list[str] = []  # 1がb個
for d in reversed(bin_C):
    # print(d)
    if d == "1":
        # XとYどちらかで1を消費
        if a > b:
            X.append("1")
            Y.append("0")
            a -= 1
        else:
            X.append("0")
            Y.append("1")
            b -= 1
        if a < 0 or b < 0:
            # aかbを使い切ってしまっていたらこの時点で不可能
            print(-1)
            exit()
    elif d == "0":
        # 1を消費する必要はないのでいったんスルー
        # この方法だとWA。答えが2^60を超えないように、早めに1を消費しておく必要があるから
        # X.append("0")
        # Y.append("0")

        # この方法だとAC
        if k > 0:
            X.append("1")
            Y.append("1")
            a -= 1
            b -= 1
            k -= 1
        else:
            X.append("0")
            Y.append("0")

# この条件は必要。aとbどちらかが極端に多いとき、消費しきれない可能性がある
if a != b:
    print(-1)
    exit()

while a + b > 0:
    X.append("1")
    Y.append("1")
    a -= 1
    b -= 1

X.reverse()
Y.reverse()
x = int("".join(X), 2)
y = int("".join(Y), 2)

# この条件はあまり本質的でないと思うが、問題に明記されているので必要！
if x >= 2**60 or y >= 2**60:
    print(-1)
    exit()

print(x, y)
