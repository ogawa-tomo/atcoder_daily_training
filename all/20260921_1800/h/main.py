# ギリギリTLE
import sys


class Player:
    def __init__(self, i: int, team: int, strength: int) -> None:
        self.i = i
        self.strength = strength
        self.team = team  # 1 or 2 or 3


N = int(input())
players: list[Player] = []
total_strength = 0
for i in range(N):
    A, B = map(int, input().split())
    player = Player(i, A, B)
    players.append(player)
    total_strength += B

if total_strength % 3 != 0:
    print(-1)
    exit()

team_strength = total_strength // 3


# dp[i][x][y]: 人iまでの所属チームを確定させ、チーム1の強さがx、チーム2の強さがyであるとき、
# 所属チームを変えた人数の最小値
dp: list[list[list[int]]] = []
for i in range(N):
    row: list[list[int]] = []
    for x in range(team_strength + 1):
        row.append([sys.maxsize] * (team_strength + 1))
    dp.append(row)

for i in range(N):
    player = players[i]
    for x in range(team_strength + 1):
        for y in range(team_strength + 1):
            # チーム1の強さがx、チーム2の強さがyであるとき

            if i == 0:
                if player.team == 1:
                    if x == player.strength and y == 0:
                        dp[i][x][y] = 0
                    elif x == 0 and y == player.strength:
                        dp[i][x][y] = 1
                    elif x == 0 and y == 0:
                        dp[i][x][y] = 1
                elif player.team == 2:
                    if x == player.strength and y == 0:
                        dp[i][x][y] = 1
                    elif x == 0 and y == player.strength:
                        dp[i][x][y] = 0
                    elif x == 0 and y == 0:
                        dp[i][x][y] = 1
                elif player.team == 3:
                    if x == player.strength and y == 0:
                        dp[i][x][y] = 1
                    elif x == 0 and y == player.strength:
                        dp[i][x][y] = 1
                    elif x == 0 and y == 0:
                        dp[i][x][y] = 0
                continue

            if player.team == 1:
                candid: list[int] = []
                if x - player.strength >= 0:
                    candid.append(dp[i - 1][x - player.strength][y])
                if y - player.strength >= 0:
                    candid.append(dp[i - 1][x][y - player.strength] + 1)
                candid.append(dp[i - 1][x][y] + 1)
                dp[i][x][y] = min(candid)
            elif player.team == 2:
                candid: list[int] = []
                if x - player.strength >= 0:
                    candid.append(dp[i - 1][x - player.strength][y] + 1)
                if y - player.strength >= 0:
                    candid.append(dp[i - 1][x][y - player.strength])
                candid.append(dp[i - 1][x][y] + 1)
                dp[i][x][y] = min(candid)
            elif player.team == 3:
                candid: list[int] = []
                if x - player.strength >= 0:
                    candid.append(dp[i - 1][x - player.strength][y] + 1)
                if y - player.strength >= 0:
                    candid.append(dp[i - 1][x][y - player.strength] + 1)
                candid.append(dp[i - 1][x][y])
                dp[i][x][y] = min(candid)

answer = dp[N - 1][team_strength][team_strength]
if answer >= sys.maxsize:
    print(-1)
else:
    print(answer)
