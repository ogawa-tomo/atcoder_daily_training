K = int(input())
A_, B_ = input().split()

A = list(map(int, list(A_)))
B = list(map(int, list(B_)))

A.reverse()
B.reverse()


A10 = 0
for i, a in enumerate(A):
    A10 += a * K**i
B10 = 0
for i, b in enumerate(B):
    B10 += b * K**i

print(A10 * B10)
