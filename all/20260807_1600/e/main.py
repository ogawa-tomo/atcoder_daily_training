N = int(input())
A = list(map(int, input().split()))
mod = 10**8

A.sort(reverse=True)
# print(A)
over_count = 0
j = N - 1
for i in range(N - 1):
    ai = A[i]
    j = max(j, i + 1)
    while True:
        aj = A[j]
        if i + 1 < j and ai + aj < mod:
            j -= 1
        else:
            break
    if ai + aj >= mod:
        over_count += j - i

# print(over_count)
answer = sum(A) * (N - 1) - mod * over_count
print(answer)
