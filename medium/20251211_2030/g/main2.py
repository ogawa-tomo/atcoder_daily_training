from collections import defaultdict, deque

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, list(input())))

    count: defaultdict[int, int] = defaultdict(int)
    count[1] = sum(S)
    count[0] = N - count[1]

    max_length: defaultdict[int, int] = defaultdict(int)

    q: deque[int] = deque()
    for s in S:
        q.append(s)
        if q[0] != s:
            q = deque([s])
        max_length[s] = max(max_length[s], len(q))

    # 全部を0にする場合と1にする場合
    answer0 = count[1] + 2 * (count[0] - max_length[0])
    answer1 = count[0] + 2 * (count[1] - max_length[1])
    print(min(answer0, answer1))
