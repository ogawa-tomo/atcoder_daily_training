from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))

for i in range(N - 1):
    a = A[i]
    next_a = A[i + 1]
    if i == 0:
        r = Fraction(next_a, a)
    else:
        if Fraction(next_a, a) != r:
            print("No")
            exit()

print("Yes")
