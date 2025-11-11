N = int(input())
A = list(map(int, input().split()))

plus_count = 0
for a in A:
    if a > 0:
        plus_count += 1

count = 0
while True:
    if plus_count <= 1:
        break
    count += 1
    A.sort(reverse=True)
    A[0] -= 1
    if A[0] == 0:
        plus_count -= 1
    A[1] -= 1
    if A[1] == 0:
        plus_count -= 1

print(count)
