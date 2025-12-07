N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()


# x円で売ってもよい売り手の数
def sellers_num(x: int):
    # ok: x円で売ってよい最大の売り手のインデックス
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if A[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok + 1


# x円で買ってよい書い手の数
def buyers_num(x: int):
    # ok: x円で買ってよい最小の書い手のインデックス
    ok = M
    ng = -1
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if B[mid] >= x:
            ok = mid
        else:
            ng = mid
    return M - ok


# ok:条件を満たす最小の値段
ok = 10**9 + 1
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if sellers_num(mid) >= buyers_num(mid):
        ok = mid
    else:
        ng = mid
print(ok)
