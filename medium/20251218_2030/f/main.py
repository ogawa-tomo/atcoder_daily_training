N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N - 1):
    a = A[i]
    ng = i
    ok = N
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if A[mid] >= a * 2:
            ok = mid
        else:
            ng = mid

    answer += N - ok


print(answer)
