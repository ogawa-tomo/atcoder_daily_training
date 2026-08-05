N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A, reverse=True)
# print(A, sorted_A)
second = sorted_A[1]
for i in range(N):
    a = A[i]
    if a == second:
        print(i + 1)
        exit()
