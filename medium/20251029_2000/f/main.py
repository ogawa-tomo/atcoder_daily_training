N = int(input())


class Section:
    def __init__(self, L: int, R: int):
        self.L = L
        self.R = R


sections: list[Section] = []
minimum = 0
maximum = 0
for _ in range(N):
    L, R = map(int, input().split())
    sections.append(Section(L, R))
    minimum += L
    maximum += R
# print(minimum, maximum)
if 0 < minimum or maximum < 0:
    print("No")
    exit()

# diffを埋めるまで、Lに値を足す
answer: list[int] = []
diff = abs(minimum)
for section in sections:
    if diff == 0:
        answer.append(section.L)
    elif section.R - section.L <= diff:
        answer.append(section.R)
        diff -= section.R - section.L
    else:
        answer.append(section.L + diff)
        diff = 0

print("Yes")
print(*answer)
