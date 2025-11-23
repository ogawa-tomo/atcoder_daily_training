N, Q = map(int, input().split())


class Player:
    def __init__(self):
        self.sent_off = False
        self.booked = False


players = [Player() for _ in range(N)]
for _ in range(Q):
    q, x = map(int, input().split())
    x -= 1
    player = players[x]
    if q == 1:
        if player.booked:
            player.sent_off = True
        else:
            player.booked = True
    elif q == 2:
        player.sent_off = True
    elif q == 3:
        if player.sent_off:
            print("Yes")
        else:
            print("No")
