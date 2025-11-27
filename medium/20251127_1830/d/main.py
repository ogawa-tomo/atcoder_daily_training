N = int(input())
A = list(map(int, input().split()))

A = list(set(A))
A.sort(reverse=True)
print(A[1])
