N, K = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

answer = 10**9
for k in range(K + 1):
    left_index = k
    right_index = N - (K - k) - 1
    diff = A[right_index] - A[left_index]
    # print(diff)
    answer = min(answer, diff)

print(answer)
