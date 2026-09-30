N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ai = 0
answer = 0
for b in B:
    while True:
        if ai >= N:
            print(-1)
            exit()
        a = A[ai]
        if a >= b:
            answer += a
            ai += 1
            break
        else:
            ai += 1
print(answer)
