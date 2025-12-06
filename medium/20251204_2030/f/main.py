N = int(input())
P = list(map(int, input().split()))


class MaxMinPoint:
    def __init__(self, before_num: int, top: bool):
        self.before_num = before_num
        self.after_num = 0
        self.top = top

    def __repr__(self):
        return str((self.before_num, self.after_num))


max_min_points: list[MaxMinPoint] = []
state = "none"  # or "up" or "down"
num = 0
for i in range(1, N):
    diff = P[i] - P[i - 1]
    if state == "none":
        num = 2
        if diff > 0:
            state = "up"
        else:
            state = "down"
    elif state == "up":
        if diff > 0:
            num += 1
        else:
            if max_min_points:
                max_min_points[-1].after_num = num - 1
            max_min_point = MaxMinPoint(num - 1, True)
            max_min_points.append(max_min_point)
            num = 2
            state = "down"
    elif state == "down":
        if diff < 0:
            num += 1
        else:
            if max_min_points:
                max_min_points[-1].after_num = num - 1
            max_min_point = MaxMinPoint(num - 1, False)
            max_min_points.append(max_min_point)
            num = 2
            state = "up"
if max_min_points:
    max_min_points[-1].after_num = num - 1

# print(max_min_points)
length = len(max_min_points)
answer = 0
for i in range(length - 1):
    p1 = max_min_points[i]
    p2 = max_min_points[i + 1]
    if p1.top:
        answer += p1.before_num * p2.after_num

print(answer)
