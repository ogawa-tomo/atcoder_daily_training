K, G, M = map(int, input().split())

grass = 0
mag = 0
for _ in range(K):
    if grass == G:
        grass = 0
    elif mag == 0:
        mag = M
    else:
        utusu = min(mag, G - grass)
        mag -= utusu
        grass += utusu
print(grass, mag)
