class Ice:
    def __init__(self, f: int, s: int):
        self.f = f
        self.s = s

    def __lt__(self, other):
        return self.s < other.s

    def __repr__(self):
        return str((self.f, self.s))


N = int(input())
ices: list[Ice] = []
for _ in range(N):
    f, s = map(int, input().split())
    ice = Ice(f, s)
    ices.append(ice)

ices.sort(reverse=True)
# print(ices)

first_ice = ices[0]
answer = 0
for i in range(1, N):
    ice = ices[i]
    if first_ice.f == ice.f:
        answer = max(answer, first_ice.s + ice.s // 2)
    else:
        answer = max(answer, first_ice.s + ice.s)

print(answer)
