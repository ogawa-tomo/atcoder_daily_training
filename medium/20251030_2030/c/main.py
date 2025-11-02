H, W = map(int, input().split())

grids: list[list[str]] = []
for _ in range(H):
    grids.append(list(input()))
# print(grids)

snuke = ["s", "n", "u", "k", "e"]

for i in range(H):
    for j in range(W):
        vi_list = [1, 1, 0, -1, -1, -1, 0, 1]
        vj_list = [0, 1, 1, 1, 0, -1, -1, -1]
        for v in range(8):
            vi = vi_list[v]
            vj = vj_list[v]
            matched = True
            for k in range(5):
                ii = i + vi * k
                jj = j + vj * k
                if ii < 0 or H <= ii or jj < 0 or W <= jj:
                    matched = False
                    break
                s = grids[ii][jj]
                if s != snuke[k]:
                    matched = False
                    break
            if matched:
                for k in range(5):
                    print(i + vi * k + 1, j + vj * k + 1)
                exit()
