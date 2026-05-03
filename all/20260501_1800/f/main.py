class Ameba:
    def __init__(self, i: int, depth: int) -> None:
        self.i = i
        self.depth = depth


N = int(input())
A = list(map(int, input().split()))
amebas = [Ameba(1, 0)]

for i, a in enumerate(A):
    index = i + 1
    parent = amebas[a - 1]
    child1 = Ameba(2 * index, parent.depth + 1)
    child2 = Ameba(2 * index + 1, parent.depth + 1)
    amebas.append(child1)
    amebas.append(child2)

for ameba in amebas:
    print(ameba.depth)
