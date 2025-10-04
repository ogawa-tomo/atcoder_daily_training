# TLE

N, K = map(int, input().split())

P = list(map(int, input().split()))

# nums[p]: pが登場するインデックス
nums = [0] * N
for i in range(N):
    p = P[i]
    nums[p - 1] = i

# print(nums)

answer = N
for i in range(N - K + 1):
    current = nums[i : i + K]
    print(current)
    # この操作でO(N)なので、全体でO(N^2)になる
    # これを高速にやるには、平衡二分探索木を使うといいらしい
    min_i = min(current)
    max_i = max(current)
    answer = min(answer, max_i - min_i)

print(answer)
