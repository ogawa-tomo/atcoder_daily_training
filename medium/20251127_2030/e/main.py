N = int(input())
S = list(input())

A_indice: list[int] = []
for i in range(2 * N):
    s = S[i]
    if s == "A":
        A_indice.append(i)

answer1 = 0
answer2 = 0
for i in range(N):
    index = i * 2
    a_index = A_indice[i]
    answer1 += abs(index - a_index)

    index = i * 2 + 1
    answer2 += abs(index - a_index)

print(min(answer1, answer2))
