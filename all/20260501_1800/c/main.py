A: list[int] = []
while True:
    try:
        a = int(input())
    except Exception:
        break
    A.append(a)
A.reverse()
for a in A:
    print(a)
