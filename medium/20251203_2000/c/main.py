N, K = map(int, input().split())

S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)

answers = S[:K]
answers.sort()
for answer in answers:
    print(answer)
