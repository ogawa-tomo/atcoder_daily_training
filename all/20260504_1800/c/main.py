N = int(input())
A = list(map(int, input().split()))
for i in range(N - 1):
    s, t = map(int, input().split())
    num = A[i] // s
    A[i] -= s * num
    A[i + 1] += t * num
print(A[N - 1])
