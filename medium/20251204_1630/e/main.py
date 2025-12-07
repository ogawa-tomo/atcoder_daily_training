H, W, N = map(int, input().split())


class Point:
    def __init__(self, i: int, a: int, b: int):
        self.i = i
        self.a = a
        self.b = b


existing_rows: list[int] = []
existing_columns: list[int] = []

points: list[Point] = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    point = Point(i, a, b)
    points.append(point)
    existing_rows.append(a)
    existing_columns.append(b)

existing_rows = list(set(existing_rows))
existing_rows.sort()
existing_columns = list(set(existing_columns))
existing_columns.sort()

# print(existing_rows, existing_columns)

for point in points:
    a = point.a
    # a未満で存在している行がいくつあるか？
    # ok: 行番号がa未満のうち最大のインデックス
    ok = -1
    ng = len(existing_rows)
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if existing_rows[mid] < a:
            ok = mid
        else:
            ng = mid
    new_a = ok + 2

    b = point.b
    # b未満で存在している列がいくつあるか？
    ok = -1
    ng = len(existing_columns)
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if existing_columns[mid] < b:
            ok = mid
        else:
            ng = mid
    new_b = ok + 2

    print(new_a, new_b)
