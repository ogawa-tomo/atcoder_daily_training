class BlackData:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x


class WhiteData:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class BlackMax:
    def __init__(self, x: int, max_y: int):
        self.x = x
        self.max_y = max_y

    def __repr__(self):
        return str((self.x, self.max_y))


N, M = map(int, input().split())
black_data_list: list[BlackData] = []
white_data_list: list[WhiteData] = []

for _ in range(M):
    data = list(input().split())
    x = int(data[0])
    y = int(data[1])
    c = data[2]

    if c == "B":
        black_data_list.append(BlackData(x, y))
    else:
        white_data_list.append(WhiteData(x, y))

black_data_list.sort(reverse=True)

# 各行について、黒の最大値を調べる
current_max = 0
black_max_list: list[BlackMax] = []
black_max_list.append(BlackMax(N + 1, 0))
for black_data in black_data_list:
    # print(black_data)
    current_max = max(current_max, black_data.y)
    black_max_list.append(BlackMax(black_data.x, current_max))
black_max_list.append(BlackMax(0, current_max))

black_max_list.reverse()
# print(black_max_list)


# 行xを与えられたとき、黒の最大値を返す
def black_max_y(x: int):
    length = len(black_max_list)

    # ok: 行の値がx以上となる最小のインデックス
    ok = length - 1
    ng = 0
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if black_max_list[mid].x >= x:
            ok = mid
        else:
            ng = mid

    return black_max_list[ok].max_y


for white_data in white_data_list:
    if black_max_y(white_data.x) >= white_data.y:
        print("No")
        exit()

print("Yes")
