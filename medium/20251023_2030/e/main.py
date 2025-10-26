N = int(input())
A = list(map(int, input().split()))

minimum = 0
num = 0
for a in A:
    num += a
    minimum = min(num, minimum)

print(num - minimum)
