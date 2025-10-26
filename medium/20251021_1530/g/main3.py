N = int(input())
S = list(input())

left: list[int] = []
right: list[int] = []

for i in range(N):
    pass
    if S[i] == "L":
        right.append(i)
    else:
        left.append(i)

left.append(N)
right.reverse()
left.extend(right)
print(" ".join([str(l) for l in left]))
