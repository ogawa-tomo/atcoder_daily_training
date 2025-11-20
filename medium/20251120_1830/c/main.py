P = list(map(int, input().split()))

alphabets = "abcdefghijklmnopqrstuvwxyz"

answer: list[str] = []
for p in P:
    answer.append(alphabets[p - 1])
print("".join(answer))
