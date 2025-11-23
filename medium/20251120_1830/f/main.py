N, K = map(int, input().split())

# score[i]: i番目の生徒の合計得点
score: list[int] = []
for _ in range(N):
    p1, p2, p3 = map(int, input().split())
    # print(sum([p1, p2, p3]))
    score.append(sum([p1, p2, p3]))

ordered_scores = sorted(score, reverse=True)
# print(score)
# print(ordered_scores)
threshold = ordered_scores[K - 1]

for i in range(N):
    if score[i] + 300 >= threshold:
        print("Yes")
    else:
        print("No")
