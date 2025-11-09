N = int(input())
A = list(map(int, input().split()))

while True:
    end = True
    for i in range(len(A) - 1):
        diff = A[i + 1] - A[i]
        if abs(diff) == 1:
            continue
        if diff > 0:
            insert = list(range(A[i] + 1, A[i + 1]))
        else:
            insert = list(range(A[i] - 1, A[i + 1], -1))
        first = A[: i + 1]
        last = A[i + 1 :]
        A = [*first, *insert, *last]
        end = False
        break
    if end:
        break
print(*A)
