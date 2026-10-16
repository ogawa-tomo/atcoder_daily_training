class Section:
    def __init__(self, left: int, right: int) -> None:
        self.left = left
        self.right = right


N, M = map(int, input().split())

sections_sorted_by_left: list[Section] = []
sections_sorted_by_right: list[Section] = []
for _ in range(N):
    l, r = map(int, input().split())
    section = Section(l, r)
    sections_sorted_by_left.append(section)
    sections_sorted_by_right.append(section)

sections_sorted_by_left.sort(key=lambda s: s.left, reverse=True)
sections_sorted_by_right.sort(key=lambda s: s.right, reverse=True)

past_sections: set[Section] = set()
answer = 0
for left in range(1, M + 1):
    while sections_sorted_by_left and sections_sorted_by_left[-1].left < left:
        past_sections.add(sections_sorted_by_left.pop())

    while sections_sorted_by_right and sections_sorted_by_right[-1] in past_sections:
        sections_sorted_by_right.pop()

    right = sections_sorted_by_right[-1].right if sections_sorted_by_right else M + 1

    answer += right - left

print(answer)
