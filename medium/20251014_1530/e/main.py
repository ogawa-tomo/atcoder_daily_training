N = int(input())
mod = 998244353

# d[n][k]: N=nのとき、最初の桁がkで始まる整数の数
d: list[list[int]] = []
d.append([])
d.append([0, 1, 1, 1, 1, 1, 1, 1, 1, 1])
for n in range(2, N + 1):
    dd: list[int] = [0]
    for k in range(1, 10):
        add = d[n - 1][k]
        if k >= 2:
            add += d[n - 1][k - 1]
        if k <= 8:
            add += d[n - 1][k + 1]
        add %= mod
        dd.append(add)
    d.append(dd)

print(sum(d[N]) % mod)
