S = list(input())

N = len(S)

answer = 0
for i in range(N - 1):
    if S[i] == S[i + 1]:
        answer += 1

if S[0] == "o":
    answer += 1
if S[N - 1] == "i":
    answer += 1

print(answer)
