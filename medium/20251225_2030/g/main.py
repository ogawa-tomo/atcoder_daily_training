import sys
from collections import deque

H, W, K = map(int, input().split())

grids: list[list[str]] = []
for _ in range(H):
    s = list(input())
    grids.append(s)

# print(grids)


class Investigator:
    def __init__(self):
        self.answer = sys.maxsize

    def investigate(self, row: list[str]):
        q: deque[str] = deque()
        current_circles = 0  # ○の数（.を置き換えたものも含む）
        current_answer = 0  # .を○に置き換えた数

        for g in row:
            q.append(g)
            if g == "o":
                current_circles += 1
            elif g == ".":
                current_circles += 1
                current_answer += 1

            while len(q) > K:
                drop = q.popleft()
                if drop == "o":
                    current_circles -= 1
                elif drop == ".":
                    current_circles -= 1
                    current_answer -= 1

            # print(q, current_circles, current_answer)
            if len(q) == current_circles == K:
                self.answer = min(self.answer, current_answer)


investigator = Investigator()

# 横向きに調べる
for i in range(H):
    row = grids[i]
    investigator.investigate(row)

# 縦向きに調べる
for j in range(W):
    column = [grids[i][j] for i in range(H)]
    investigator.investigate(column)

if investigator.answer == sys.maxsize:
    print(-1)
else:
    print(investigator.answer)
