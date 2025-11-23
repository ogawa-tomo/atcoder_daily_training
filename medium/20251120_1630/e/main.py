N = int(input())
mod = 998244353
answer = 0
digits = len(str(N))
for digit in range(1, digits + 1):
    if digit != digits:
        max_value = 9 * 10 ** (digit - 1)
    else:
        max_value = N - (10 ** (digit - 1) - 1)
    answer += (1 + max_value) * max_value // 2
    answer %= mod

print(answer)
