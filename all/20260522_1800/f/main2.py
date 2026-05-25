N = int(input())
A = list(map(int, input().split()))

answer: list[int] = []
for a in A:
    answer.append(a)
    length = len(answer)
    if (
        length >= 4
        and answer[length - 1] == answer[length - 2]
        and answer[length - 1] == answer[length - 3]
        and answer[length - 1] == answer[length - 4]
    ):
        # answer = answer[: length - 4] # これだとTLE
        for _ in range(4):
            answer.pop()

print(len(answer))
