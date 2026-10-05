# だめ
from fractions import Fraction

N = int(input())
MOD = 998244353


def f(e: Fraction):
    denominator = pow(e.denominator, -1, MOD)
    return e.numerator * denominator % MOD


# max_num = 100

A_list: list[list[int]] = []
nums: set[int] = set()
for _ in range(N):
    A = list(map(int, input().split()))
    A.sort()
    A_list.append(A)
    for a in A:
        nums.add(a)

num_list = list(nums)
num_list.sort()
max_num = len(num_list)

# index[n]: 数字nのインデックス
index: dict[int, int] = dict()
for i in range(max_num):
    n = num_list[i]
    index[n] = i

max_num = 100  # これが10**9になっちゃう

# p_list[i]: すべてi以下である確率
p_list: list[Fraction] = [Fraction(1, 1)] * max_num
p_list[0] = Fraction(0, 1)
for A in A_list:
    row: list[Fraction] = [Fraction(0, 1)] * max_num  # row[i]: iが出る確率
    i = 0
    while i < 6:
        a = A[i]
        repeat = 1
        while i < 5 and A[i + 1] == a:
            i += 1
            repeat += 1
        p = Fraction(repeat, 6)
        row[a] = p
        # row[index[a]] = p

        i += 1
    # print(row)
    # row[i]: i以下が出る確率
    for i in range(1, max_num):
        row[i] += row[i - 1]
    # print(row)

    for i in range(1, max_num):
        p_list[i] *= row[i]

# print(p_list)

answer = Fraction(0, 1)
for i in range(1, max_num):
    answer += i * (p_list[i] - p_list[i - 1])
# for j in range(max_num):
#     n = num_list[j]
#     if j == 0:
#         answer += n * p_list[index[n]]
#     else:
#         prev_n = num_list[j - 1]
#         answer += n * (p_list[index[n]] - p_list[index[prev_n]])
# print(answer)
print(f(answer))
