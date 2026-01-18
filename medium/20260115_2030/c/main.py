N = int(input())
S = list(map(int, input().split()))

candidates: set[int] = set()

for a in range(1, 1000):
    for b in range(1, 1000):
        v = 4 * a * b + 3 * a + 3 * b
        if v > 1000:
            continue
        candidates.add(v)

# print(candidates)


answer = 0
for s in S:
    if s not in candidates:
        answer += 1

print(answer)
