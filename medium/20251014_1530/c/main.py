# TLE
N, S = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

answer = 0
for i in range(N - 1):
    a = A[i]
    rest = A[i + 1 :]
    # print(a, rest)
    length = N - i - 1
    target = S - a

    # ok:合計がS以下である最大のインデックス
    ok = -1
    ng = length
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if rest[mid] <= target:
            ok = mid
        else:
            ng = mid
    # ok2: 合計がS以上である最小のインデックス
    ok2 = length
    ng2 = -1
    while ok2 - ng2 > 1:
        mid = (ok2 + ng2) // 2
        if rest[mid] >= target:
            ok2 = mid
        else:
            ng2 = mid

    if ok2 <= ok:
        answer += ok - ok2 + 1

print(answer)
