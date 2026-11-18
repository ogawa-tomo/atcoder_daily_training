import sys
from typing import Callable


# 二分探索
def most_right_ok(min_i: int, max_i: int, ok_func: Callable[[int], bool]):
    ok = min_i - 1
    ng = max_i + 1
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if ok_func(mid):
            ok = mid
        else:
            ng = mid
    if ok < min_i:
        return None
    return ok


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
# print(A)
# print(B)

answer = sys.maxsize
for i in range(N):
    a = A[i]
    # a-b>=0となる最も右側のインデックス
    j = most_right_ok(0, M - 1, lambda j: a - B[j] >= 0)

    if j is None:
        answer = min(answer, abs(a - B[0]))
    else:
        answer = min(answer, abs(a - B[j]))
        if j < M - 1:
            answer = min(answer, abs(a - B[j + 1]))

print(answer)
