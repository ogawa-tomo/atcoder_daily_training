from collections import defaultdict


N, M = map(int, input().split())
A = list(map(int, input().split()))

current_candid = 0
max_votes_num = 0
vote_num_by_candid: defaultdict[int, int] = defaultdict(int)
for a in A:
    vote_num_by_candid[a] += 1
    current_votes_num = vote_num_by_candid[a]
    if current_votes_num > max_votes_num:
        max_votes_num = current_votes_num
        current_candid = a
    elif current_votes_num == max_votes_num:
        current_candid = min(current_candid, a)
    print(current_candid)
