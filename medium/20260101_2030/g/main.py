from collections import defaultdict

N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

x_list: list[int] = []
y_list: list[int] = []

for i in range(1, N):
    a = A[i]
    if i % 2 == 0:
        x_list.append(a)
    else:
        y_list.append(a)

# print(x_list, y_list)
x_length = len(x_list)
y_length = len(y_list)

# x_dp[i]: i回目までの移動で行けるところはTrue、行けないところはFalse
x_dp: list[defaultdict[int, bool]] = []
for i in range(x_length + 1):
    x_dp.append(defaultdict(bool))
x_dp[0][A[0]] = True
y_dp: list[defaultdict[int, bool]] = []
for i in range(y_length + 1):
    y_dp.append(defaultdict(bool))
y_dp[0][0] = True
# print(x_dp, y_dp)


def calc(xy_list: list[int], xy_dp: list[defaultdict[int, bool]]):
    for i, xy in enumerate(xy_list):
        origin = xy_dp[i]
        destin = xy_dp[i + 1]
        for o in origin:
            destin[o + xy] = True
            destin[o - xy] = True


calc(x_list, x_dp)
calc(y_list, y_dp)
# print(x_dp[x_length])
# print(y_dp[y_length])

if x_dp[x_length][X] and y_dp[y_length][Y]:
    print("Yes")
else:
    print("No")
