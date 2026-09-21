N, K, M = map(int, input().split())


class Gewel:
    def __init__(self, color: int, value: int) -> None:
        self.color = color
        self.value = value
        self.selected = False


gewels: list[Gewel] = []
for _ in range(N):
    c, v = map(int, input().split())
    gewel = Gewel(c, v)
    gewels.append(gewel)

gewels.sort(key=lambda g: g.value, reverse=True)

answer = 0
selected_num = 0

# まずは各色で最大のものをとる
selected_colors: set[int] = set()
for gewel in gewels:
    if gewel.color not in selected_colors:
        answer += gewel.value
        selected_colors.add(gewel.color)
        gewel.selected = True
        selected_num += 1
        if len(selected_colors) == M:
            break

# 残りでとれるだけとる
for gewel in gewels:
    if selected_num >= K:
        break
    if gewel.selected:
        continue
    answer += gewel.value
    selected_num += 1

print(answer)
