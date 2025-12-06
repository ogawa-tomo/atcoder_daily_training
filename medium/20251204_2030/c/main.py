S = list(input())

sections: list[str] = []
for i, s in enumerate(S):
    if s == ".":
        continue
    sections.append(str(i + 1))
    if len(sections) == 2:
        print(",".join(sections))
        sections = []
