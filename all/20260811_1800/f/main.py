N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
answer = 0
bi = 0
for a in A:
    while True:
        if bi >= M:
            break
        b = B[bi]
        if b <= 2 * a:
            answer += 1
            bi += 1
            break
        else:
            bi += 1

print(answer)
