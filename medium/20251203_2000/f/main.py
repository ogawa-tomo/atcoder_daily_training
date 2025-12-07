N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

# 買った箱の大きさ
bought_box = 0
bought = 0  # 箱を買ったら1
# 箱iにおもちゃが入るかを調べる
for i in range(N - 1):
    toy = A[i + bought]
    box = B[i]
    if box >= toy:
        continue
    if bought == 1:
        print(-1)
        exit()
    # おもちゃの大きさの箱を買う
    bought_box = toy
    bought = 1
    # 今見てる箱に次のおもちゃが入るかをチェック
    toy = A[i + bought]
    box = B[i]
    if box < toy:
        print(-1)
        exit()

# まだ箱を買ってなければ、一番小さいおもちゃの大きさの箱を買う
if bought == 0:
    bought_box = A[N - 1]

print(bought_box)
