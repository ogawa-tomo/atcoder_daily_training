S = list(input())
N = len(S)
# for s in S:
#     print(ord(s))

answer = 0
for i in range(1, N):
    answer += 26**i
for j in range(N - 1, -1, -1):
    s = S[N - 1 - j]  # 右からj文字目
    n = ord(s) - 65  # A: 0, Z: 25
    answer += n * 26**j
print(answer + 1)
