class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


points: list[Point] = []
for _ in range(4):
    x, y = map(int, input().split())
    points.append(Point(x, y))

for i in range(4):
    point = points[i]
    right_point = points[(i + 1) % 4]
    left_point = points[(i - 1) % 4]
    v_right_x = right_point.x - point.x
    v_right_y = right_point.y - point.y
    v_left_x = left_point.x - point.x
    v_left_y = left_point.y - point.y

    # 行列式
    if v_right_x * v_left_y - v_left_x * v_right_y <= 0:
        print("No")
        exit()
print("Yes")
