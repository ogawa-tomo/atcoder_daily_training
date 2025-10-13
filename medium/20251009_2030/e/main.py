import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(A)

answer = sys.maxsize
for i in range(K + 1):
    # print(A[i], A[N - 1 - K + i])
    answer = min(answer, A[N - 1 - K + i] - A[i])
print(answer)
