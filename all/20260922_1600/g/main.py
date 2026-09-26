from collections import defaultdict


class Player:
    def __init__(self) -> None:
        self.score = 0


N, T = map(int, input().split())

players = [Player() for _ in range(N)]
# d[x]: 点数xの選手の人数
d: defaultdict[int, int] = defaultdict(int)
d[0] = N
answer = 1
for _ in range(T):
    a, b = map(int, input().split())
    a -= 1
    player = players[a]
    d[player.score] -= 1
    if d[player.score] == 0:
        answer -= 1
    player.score += b
    d[player.score] += 1
    if d[player.score] == 1:
        answer += 1
    print(answer)
