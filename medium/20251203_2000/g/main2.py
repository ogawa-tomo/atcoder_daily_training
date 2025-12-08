N = int(input())
mod = 998244353

digits = len(str(N))


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


def calc(n):
    if n == 1:
        return N % mod
    if n % 2 == 0:
        t = calc(n // 2)
        return (t * repeatedSquare(10, (n // 2) * digits, mod) + t) % mod
    return (calc(n - 1) * 10**digits + N) % mod


print(calc(N))
