N = int(input())
A = list(map(int, input().split()))

A.sort()
total = sum(A)

small_num = total // N
large_num = small_num + 1

large_num_num = total - small_num * N
small_num_num = N - large_num_num

# print(small_num, large_num)
# print(small_num_num, large_num_num)

answer = 0
for i in range(N):
    a = A[i]
    if i < small_num_num:
        answer += abs(a - small_num)
    else:
        answer += abs(a - large_num)

answer //= 2
print(answer)
