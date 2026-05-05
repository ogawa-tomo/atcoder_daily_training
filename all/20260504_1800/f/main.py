N = int(input())
mod = 998244353
digit_length = len(str(N))
# print(digit_length)

answer = 0
for digit in range(1, digit_length + 1):
    if digit < digit_length:
        max_num = 9 * 10 ** (digit - 1)
    else:
        max_num = N - (10 ** (digit - 1) - 1)
    # print(digit, max_num)
    max_num %= mod
    answer += max_num * (max_num + 1) // 2
    answer %= mod
print(answer)
