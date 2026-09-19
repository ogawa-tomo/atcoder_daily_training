N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

answer = 0
bi = 0
for a in A:
    if bi >= M:
        break
    b = B[bi]
    if b <= a * 2:
        answer += 1
        bi += 1

print(answer)
