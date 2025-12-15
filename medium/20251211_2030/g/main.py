# WA
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, list(input())))
    mid = N // 2

    standard = S[mid]
    min_standard_index = mid
    while True:
        if min_standard_index == 0 or S[min_standard_index - 1] != standard:
            break
        min_standard_index -= 1
    max_standard_index = mid
    while True:
        if max_standard_index == N - 1 or S[max_standard_index + 1] != standard:
            break
        max_standard_index += 1

    answer = 0
    for i in range(min_standard_index):
        answer += 1
        if S[i] == standard:
            answer += 1

    for j in range(N - 1, max_standard_index, -1):
        answer += 1
        if S[j] == standard:
            answer += 1

    print(answer)
