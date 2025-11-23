N = int(input())
S = list(map(int, list(input())))

one_num = 0
for s in S:
    if s:
        one_num += 1

if one_num == 1:
    print(0)
    exit()
mid_one = (one_num + 1) // 2

mid_one_index = 0
one_count = 0
for i in range(N):
    s = S[i]
    if s:
        one_count += 1
        if one_count == mid_one:
            mid_one_index = i
            break

# print(mid_one_index)

answer = 0

# 右側の1を寄せる
right_one_count = 0
for i in range(mid_one_index + 1, N):
    s = S[i]
    if not s:
        continue
    answer += i - mid_one_index - 1 - right_one_count
    right_one_count += 1

# 左側の1を寄せる
left_one_count = 0
for i in range(mid_one_index - 1, -1, -1):
    s = S[i]
    if not s:
        continue
    answer += mid_one_index - i - 1 - left_one_count
    left_one_count += 1

print(answer)
