N, M = map(int, input().split())
S: list[set[int]] = []
for _ in range(M):
    c = int(input())
    s = set(map(int, input().split()))
    S.append(s)

all_nums = set(range(1, N + 1))
# print(S)
answer = 0
for i in range(1 << M):
    # i: 選んだ集合を表すビット列
    nums: set[int] = set()
    for j in range(M):
        # j 番目の集合が選ばれているかを判定し、選ばれていれば数字の集合に含める
        if 1 << j & i:
            nums |= S[j]
    if nums == all_nums:
        answer += 1

print(answer)
