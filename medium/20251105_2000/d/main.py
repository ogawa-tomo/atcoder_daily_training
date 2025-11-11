import math

X = int(input())
for n in range(100):
    if math.factorial(n) == X:
        print(n)
        exit()
