N = int(input())
p = list(map(int, input().split()))

# joy_num[n]: n回の操作を行ったとき、喜ぶ人の数
joy_num = [0] * N

# それぞれの料理について、喜ぶ人が出る操作回数を記録していく
for i in range(N):
    distance = (p[i] - i) % N
    distance_plus_1 = (distance + 1) % N
    distance_minus_1 = (distance - 1) % N
    joy_num[distance] += 1
    joy_num[distance_plus_1] += 1
    joy_num[distance_minus_1] += 1

print(max(joy_num))
