# TLE
# なんで？O(Nlog(N))でできてると思ったのだが…
N = int(input())
A = list(map(int, input().split()))
mod = 10**8

A.sort(reverse=True)

# 足すとmodを超える組み合わせの数
over_count = 0
for i in range(N - 1):
    a = A[i]
    residue_list = A[i + 1 :]
    # residue_listのうち、aに足したらmodを超えるものがいくつあるかを調べる
    length = len(residue_list)
    # ok: a + residue_list[ok] >= mod となる最大の値を２分探索で調べる
    ok = -1
    ng = length
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if a + residue_list[mid] >= mod:
            ok = mid
        else:
            ng = mid
    over_count += ok + 1

print(sum(A) * (N - 1) - mod * over_count)
