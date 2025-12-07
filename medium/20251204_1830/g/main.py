import sys
from typing import Literal

N = int(input())
S = list(input())

Hand = Literal["R", "S", "P"]
hands: list[Hand] = ["R", "S", "P"]

Result = Literal["win", "lose", "draw"]


def result(me: Hand, opponent: str) -> Result:
    if me == "R":
        if opponent == "R":
            return "draw"
        elif opponent == "S":
            return "win"
        elif opponent == "P":
            return "lose"
    elif me == "S":
        if opponent == "R":
            return "lose"
        elif opponent == "S":
            return "draw"
        elif opponent == "P":
            return "win"
    elif me == "P":
        if opponent == "R":
            return "win"
        elif opponent == "S":
            return "lose"
        elif opponent == "P":
            return "draw"
    raise


# dp[i][H]: i回目に出した手がHのとき、勝つ回数の最大値
dp: list[dict[Hand, int]] = []
for i, s in enumerate(S):
    d: dict[Hand, int] = {}
    if i == 0:
        for hand in hands:
            res = result(hand, s)
            if res == "win":
                d[hand] = 1
            elif res == "draw":
                d[hand] = 0
            elif res == "lose":
                d[hand] = -sys.maxsize
        dp.append(d)
        continue

    for hand in hands:
        res = result(hand, s)

        # 負けは論外
        if res == "lose":
            d[hand] = -sys.maxsize
            continue

        # あいこか勝ちの場合は、直前の3パターンを調べて最大値を出す
        max_point = -sys.maxsize
        for prev_hand in hands:
            if prev_hand == hand:
                # 前と同じ手はだめ
                continue
            max_point = max(max_point, dp[i - 1][prev_hand])
        d[hand] = max_point
        if res == "win":
            d[hand] += 1

    dp.append(d)

# print(dp)
print(max(dp[N - 1]["P"], dp[N - 1]["R"], dp[N - 1]["S"]))
