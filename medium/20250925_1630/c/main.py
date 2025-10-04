X = int(input())
# print(X)
# print(X % 10)
amari = X % 10

if amari != 0:
    X += 10 - amari

print(X // 10)
