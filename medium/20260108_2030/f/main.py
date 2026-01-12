import math

N = int(input())
A = list(map(int, input().split()))
mod = 10**8

total = (N - 1) * sum(A)
# print(total)

A.sort(reverse=True)
# print(A)

# 合計がmodを超える組み合わせの数を求める
num = 0
for i in range(N - 1):
    a = A[i]
    ok = i
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if a + A[mid] >= mod:
            ok = mid
        else:
            ng = mid

    num_i = ok - i
    num += num_i

print(total - num * mod)
