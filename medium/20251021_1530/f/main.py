N, M, K = map(int, input().split())
mod = 998244353


def f(n: int, m: int, k: int):
    if n == 1:
        if m >= k and k >= 1:
            return k
        else:
            return 0
    answer = 0
    for i in range(1, min(m + 1, k + 1)):
        answer += f(n - 1, m, k - i)
        answer %= mod
    return answer % mod


print(f(N, M, K) % mod)
