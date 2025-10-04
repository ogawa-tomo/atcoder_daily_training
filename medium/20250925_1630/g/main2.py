# WA
import heapq

N, K = map(int, input().split())

P = list(map(int, input().split()))

# nums[p]: pが登場するインデックス
nums = [0] * N
for i in range(N):
    p = P[i]
    nums[p - 1] = i

print(nums)

current = nums[:K]
min_heap: list[int] = current
heapq.heapify(min_heap)
max_heap: list[int] = [-c for c in current]
heapq.heapify(max_heap)
# print(min_heap, max_heap)
min_i = min_heap[0]
max_i = -max_heap[0]
answer = max_i - min_i
for start in range(1, N - K + 1):
    end = start + K - 1
    # print(start, end)
    print(nums[start : end + 1])
    remove_i = nums[start - 1]
    add_i = nums[end]
    if remove_i == min_i:
        heapq.heappop(min_heap)
    elif remove_i == max_i:
        heapq.heappop(max_heap)
    heapq.heappush(min_heap, add_i)
    heapq.heappush(max_heap, -add_i)
    print(min_heap, max_heap)
    # これだと正しい最小値・最大値を求められない
    min_i = min_heap[0]
    max_i = -max_heap[0]
    answer = min(answer, max_i - min_i)

    # current = nums[start : end + 1]
    # min_i = min(current)
    # max_i = max(current)
    # answer = min(answer, max_i - min_i)

print(answer)
