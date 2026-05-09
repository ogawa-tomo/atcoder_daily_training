N = int(input())
A = list(map(int, input().split()))
for i, a in enumerate(A):
    answer = -1
    for j in range(i - 1, -1, -1):
        if A[j] > a:
            answer = j + 1
            break
    print(answer)
