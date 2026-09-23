class Section:
    def __init__(self, l: int, r: int) -> None:
        self.l = l
        self.r = r


N = int(input())

sections: list[Section] = []
min_s = 0
max_s = 0
for _ in range(N):
    l, r = map(int, input().split())
    section = Section(l, r)
    sections.append(section)
    min_s += l
    max_s += r

if max_s < 0 or 0 < min_s:
    print("No")
    exit()

surplus = max_s
answer: list[int] = []
for section in sections:
    if surplus == 0:
        answer.append(section.r)
    else:
        add_num = max(section.r - surplus, section.l)
        answer.append(add_num)
        surplus -= section.r - add_num

print("Yes")
print(*answer)
# print(sum(answer))
