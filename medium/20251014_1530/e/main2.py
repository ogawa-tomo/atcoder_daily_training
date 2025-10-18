N = int(input())
mod = 998244353

# d[n][k]: N=nのとき、最初の桁がkで始まる整数の数
d: dict[int, dict[int, int]] = {}
d[1] = {}
for i in range(1, 10):
    d[1][i] = 1

for n in range(2, N + 1):
    dd: dict[int, int] = {}
    for k in range(1, 10):
        value = d[n - 1][k]
        if k >= 2:
            value += d[n - 1][k - 1]
        if k <= 8:
            value += d[n - 1][k + 1]
        value %= mod
        dd[k] = value
    d[n] = dd

print(sum(d[N].values()) % mod)
