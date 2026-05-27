N, M = map(int, input().split())
S: list[list[int]] = []
for _ in range(M):
    c = int(input())
    s = list(map(int, input().split()))
    S.append(s)

# print(S)
answer = 0
for i in range(1 << M):
    # i: 選んだ集合を表すビット列
    nums: set[int] = set()
    for j in range(M):
        # j 番目の集合が選ばれているかを判定し、選ばれていれば数字の集合に含める
        if 1 << j & i:
            for n in S[j]:
                nums.add(n)

    included = True
    for x in range(1, N + 1):
        if x not in nums:
            included = False
            break
    if included:
        answer += 1

print(answer)
