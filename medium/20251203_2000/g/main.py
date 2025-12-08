N = int(input())
mod = 998244353


def repeatedSquare(num: int, pow: int, mod: int):
    a = num
    b = pow
    answer = 1
    while b > 0:
        # i回目のループで、bが2^iの成分を持っていれば、掛け算をする
        if b & 1:
            answer *= a
            answer %= mod
        # i回目のループでは、a^(2^i)をかける（0回目: a^1, 1回目: a^2, 2回目: a^4, ...）
        a *= a
        a %= mod
        b >>= 1
    return answer


def fraction_mod(numerator: int, denominator: int, mod: int):
    if denominator % mod == 0:
        raise
    return numerator * repeatedSquare(denominator, mod - 2, mod) % mod


length = len(str(N))
r = 10**length

# r**N
rN = repeatedSquare(r, N, mod)

# vn = N * (r**N - 1) // (r - 1) # これは計算できない
print(fraction_mod(N * (rN - 1), r - 1, mod))
