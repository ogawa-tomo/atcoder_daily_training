S = input()

answer: list[str] = []
for s in S:
    answer.append(s)
    if s == "C" and len(answer) >= 3 and answer[-2] == "B" and answer[-3] == "A":
        for _ in range(3):
            answer.pop()

print("".join(answer))
