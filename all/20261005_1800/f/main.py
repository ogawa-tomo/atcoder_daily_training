from collections import defaultdict


N, K = map(int, input().split())

S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)


alphabets = "abcdefghijklmnopqrstuvwxyz"

answer = 0
for i in range(1 << N):
    # i: 文字列を選ぶパターン
    # d[s]: 文字sが登場した回数
    d: defaultdict[str, int] = defaultdict(int)
    for j in range(N):
        if i & (1 << j):
            s = S[j]
            for c in s:
                d[c] += 1

    count = 0
    for c in alphabets:
        if d[c] == K:
            count += 1
    answer = max(answer, count)

print(answer)
