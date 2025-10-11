S = list(input())
T = list(input())

length = len(S)

# 置き換えると辞書順で小さくなる文字のインデックス
indice1: list[int] = []
# 置き換えると辞書順で大きくなる文字のインデックス
indice2: list[int] = []
for i in range(length):
    s = S[i]
    t = T[i]
    if s > t:
        indice1.append(i)
    elif s < t:
        indice2.append(i)

indice2.reverse()

print(len(indice1) + len(indice2))
for i in indice1:
    S[i] = T[i]
    print("".join(S))
for i in indice2:
    S[i] = T[i]
    print("".join(S))
