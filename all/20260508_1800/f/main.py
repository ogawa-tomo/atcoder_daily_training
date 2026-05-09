S = list(input())
N = len(S)
# for s in S:
#     print(ord(s))
answer = 0
for i in range(N):
    s = S[N - 1 - i]  # 右からi文字目
    n = ord(s) - 64
    answer += n * 26**i
print(answer)
