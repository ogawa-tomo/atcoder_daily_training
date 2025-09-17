N = int(input())
A = list(map(int, input().split()))

# emerged_num[i]: iのカードの枚数
emerged_num = [0] * (N + 1)
for a in A:
    emerged_num[a] += 1

for i in range(N + 1):
    if emerged_num[i] == 3:
        print(i)
        exit()