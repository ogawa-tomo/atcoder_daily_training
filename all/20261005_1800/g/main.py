import heapq
from collections import defaultdict


N, M = map(int, input().split())
A = list(map(int, input().split()))

# 票数ごとの候補者優先度キュー
candid_queue_by_vote: defaultdict[int, list[int]] = defaultdict(list)
# 候補者ごとの票数
vote_by_candidate: defaultdict[int, int] = defaultdict(int)
# 現在の最大票数
max_vote = 0

for a in A:
    vote_by_candidate[a] += 1
    current_vote = vote_by_candidate[a]
    heapq.heappush(candid_queue_by_vote[current_vote], a)
    max_vote = max(max_vote, current_vote)
    print(candid_queue_by_vote[max_vote][0])
