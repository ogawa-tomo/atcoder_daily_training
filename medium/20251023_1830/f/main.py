N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
# print(A)
# print(B)

answer = 0
plus = 0
for i in range(N - 1):
    # i番目に大きい箱に、i番目に大きいおもちゃを入れる
    omocha = A[i + plus]
    hako = B[i]
    if hako >= omocha:
        continue
    if plus == 1:
        print(-1)
        exit()
    plus = 1
    answer = omocha
    omocha = A[i + plus]
    if hako >= omocha:
        continue
    else:
        print(-1)
        exit()
if plus == 1:
    print(answer)
else:
    print(A[N - 1])
