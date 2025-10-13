N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)
# print(A, B)


# x円のときの売り手の人数
def num_sell(x: int):
    # ok: x以下で最大のインデックス
    ok = -1
    ng = N
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if A[mid] <= x:
            ok = mid
        else:
            ng = mid
    return ok + 1


# x円のときの買い手の人数
def num_buy(x: int):
    # ok: x以上で最大のインデックス
    ok = -1
    ng = M
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if B[mid] >= x:
            ok = mid
        else:
            ng = mid
    return ok + 1


# ok: 売り手が買い手より多い最小の値段
ok = 10**9 + 1
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if num_sell(mid) >= num_buy(mid):
        ok = mid
    else:
        ng = mid

print(ok)
