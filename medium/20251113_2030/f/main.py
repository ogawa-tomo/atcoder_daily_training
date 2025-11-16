N = int(input())
A = list(map(int, input().split()))
mod = 10**8

# 明らかにTLE
# answer = 0
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         answer += (A[i] + A[j]) % mod
# print(answer)

A.sort()
over_mod_pairs = 0
# print(A)
for i in range(N - 1):
    a = A[i]
    # インデックスがi+1~N-1で、足すとmodを超えるものの数
    ok = N  # 足すとmodを超える最小のインデックス
    ng = i
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if a + A[mid] >= mod:
            ok = mid
        else:
            ng = mid
    over_mod_pairs += N - ok

print((N - 1) * sum(A) - mod * over_mod_pairs)
