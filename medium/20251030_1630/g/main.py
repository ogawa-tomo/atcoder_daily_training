N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

# 各iについてmin(Ai, P)を足し合わせたものをsumとすると、P*K <= sumならばP個のプロジェクトを作ることができる

ok = 0
ng = 10**18
while ng - ok > 1:
    mid = (ng + ok) // 2
    s = 0
    for a in A:
        s += min(a, mid)
    if s >= K * mid:
        ok = mid
    else:
        ng = mid

print(ok)
