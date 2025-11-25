from fractions import Fraction
import sys
import heapq
import math


class JumpBoard:
    def __init__(self, x: int, y: int, p: int):
        self.x = x
        self.y = y
        self.p = p
        self.links: list[Link] = []
        # 起点からそこにたどり着くのに必要なジャンプ力
        self.needed_s = sys.maxsize
        self.finalized = False

    def __repr__(self):
        return str(self.needed_s)


def skill(from_jb: JumpBoard, to_jb: JumpBoard):
    distance = abs(from_jb.x - to_jb.x) + abs(from_jb.y - to_jb.y)
    return math.ceil(Fraction(distance, from_jb.p))


class QueueObject:
    def __init__(self, jump_board: JumpBoard):
        self.jump_board = jump_board
        self.needed_s = jump_board.needed_s

    def __lt__(self, other):
        return self.needed_s < other.needed_s

    def __repr__(self):
        return str(self.needed_s)


class Link:
    def __init__(self, needed_s: int, to_jump_board: JumpBoard):
        self.needed_s = needed_s
        self.to_jump_board = to_jump_board


def dijkstra(start_jump_board: JumpBoard):
    q: list[QueueObject] = []
    start_jump_board.needed_s = 0

    heapq.heappush(q, QueueObject(start_jump_board))
    while q:
        queue_object = heapq.heappop(q)
        jump_board = queue_object.jump_board

        if jump_board.finalized:
            continue
        jump_board.finalized = True

        for link in jump_board.links:
            needed_s = max(jump_board.needed_s, link.needed_s)
            if needed_s < link.to_jump_board.needed_s:
                link.to_jump_board.needed_s = needed_s
                heapq.heappush(q, QueueObject(link.to_jump_board))


N = int(input())

jump_boards: list[JumpBoard] = []
for _ in range(N):
    x, y, p = map(int, input().split())
    jb = JumpBoard(x, y, p)
    jump_boards.append(jb)

for from_jb in jump_boards:
    for to_jb in jump_boards:
        if from_jb == to_jb:
            continue
        needed_s = skill(from_jb, to_jb)
        link = Link(needed_s, to_jb)
        from_jb.links.append(link)


def reset():
    for jb in jump_boards:
        jb.finalized = False
        jb.needed_s = sys.maxsize


min_needed_skill = sys.maxsize
for start in jump_boards:
    reset()
    dijkstra(start)
    needed_skill = 0
    for jb in jump_boards:
        if jb == start:
            continue
        # print(jb.needed_s)
        needed_skill = max(jb.needed_s, needed_skill)
    min_needed_skill = min(min_needed_skill, needed_skill)

print(min_needed_skill)
