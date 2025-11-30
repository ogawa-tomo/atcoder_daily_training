S = list(input())
K = int(input())


if "X" not in S and K == 0:
    print(0)
    exit()

N = len(S)
k = 0
right_i = 0
answer = 0
for left_i in range(N):
    left = S[left_i]

    # 仕切り直し
    if right_i <= left_i:
        right_i = left_i
        if left == ".":
            k = 1
            if K == 0:
                continue
        else:
            k = 0

    while True:
        if right_i == N - 1:
            break
        if k >= K and S[right_i + 1] == ".":
            break
        right_i += 1
        right = S[right_i]
        if right == ".":
            k += 1

    answer = max(answer, right_i - left_i + 1)

    if left == ".":
        k -= 1

print(answer)
