class Section:
    def __init__(self, l: int, r: int) -> None:
        self.l = l
        self.r = r


N = int(input())

sections: list[Section] = []
for _ in range(N):
    l, r = map(int, input().split())
    sections.append(Section(l, r))

sections.sort(key=lambda s: s.l)
answer = 0
for i in range(N):
    section = sections[i]
    # ok: leftがこのセクションのright以下であるようなセクションのインデックス
    ok = i
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if sections[mid].l <= section.r:
            ok = mid
        else:
            ng = mid
    answer += ok - i

print(answer)
