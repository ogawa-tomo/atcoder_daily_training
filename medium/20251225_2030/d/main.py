H, W = map(int, input().split())


class Piece:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j


pieces: list[Piece] = []
for i in range(H):
    data = list(input())
    for j, d in enumerate(data):
        if d == "o":
            pieces.append(Piece(i, j))

print(abs(pieces[0].i - pieces[1].i) + abs(pieces[0].j - pieces[1].j))
