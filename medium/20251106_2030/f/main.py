N, K, X = map(int, input().split())
A = list(map(int, input().split()))

# まず、すべての商品について、値段が負にならない程度にクーポンをできるだけ使う
for i in range(N):
    # 値段が負にならない程度に、使えるクーポン枚数
    possible_use_num = A[i] // X
    if possible_use_num <= K:
        # 全部使えるなら、使う
        K -= possible_use_num
        A[i] -= possible_use_num * X
    else:
        # 使えないなら、使えるだけ使う
        A[i] -= K * X
        K = 0

# クーポンを使い切っていれば、それが答え
if K == 0:
    print(sum(A))
    exit()

A.sort(reverse=True)
# 値段が高いほうから、クーポンを使えるだけ使う
for i in range(N):
    A[i] = 0
    K -= 1
    if K == 0:
        break
print(sum(A))
