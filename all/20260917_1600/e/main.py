N = int(input())
H = list(map(int, input().split()))

answer = 1
for gap in range(1, N):
    answer_by_gap = 1
    # dp[i]: 間隔gapでi番目のビルにちょうど到達したとき、選べているビルの数
    dp: list[int] = []
    for i in range(N):
        if i - gap < 0:
            dp.append(1)
        elif H[i - gap] == H[i]:
            num = dp[i - gap] + 1
            dp.append(num)
            answer_by_gap = max(answer_by_gap, num)
        else:
            dp.append(1)
    answer = max(answer, answer_by_gap)

print(answer)
