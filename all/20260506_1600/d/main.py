X = int(input())

q = X // 10
r = X % 10
if r == 0:
    print(q)
else:
    print(q + 1)
