S = list(input())
N = len(S)

answer = 0
for i in range(N - 2):
    si = S[i]
    if si == "A":
        for j in range(i + 1, N - 1):
            sj = S[j]
            if sj == "B":
                k = j + (j - i)
                if k <= N - 1 and S[k] == "C":
                    answer += 1

print(answer)
