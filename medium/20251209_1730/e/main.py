N = int(input())

L = 12
elements = [int("1" * (i + 1)) for i in range(L)]
s: set[int] = set()
for i in range(L):
    for j in range(L):
        for k in range(L):
            s.add(elements[i] + elements[j] + elements[k])

repunits = list(s)
repunits.sort()
print(repunits[N - 1])
