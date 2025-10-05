N = int(input())
A = list(map(int, input().split()))
mod = 10**8
# mod = 10

A.sort(reverse=True)
# print(A)

# 足すとmodを超える組み合わせの数を尺取法で調べる
over_count = 0
max_index = N - 1
for i in range(N - 1):
    if max_index <= i:
        break
    while True:
        if A[i] + A[max_index] >= mod:
            break
        max_index -= 1
        if max_index == i:
            break
    over_count += max_index - i

print(sum(A) * (N - 1) - mod * over_count)
