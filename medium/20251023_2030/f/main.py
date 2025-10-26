h1, h2, h3, w1, w2, w3 = map(int, input().split())

answer = 0
for n11 in range(1, 29):
    for n12 in range(1, 29):
        for n21 in range(1, 29):
            for n22 in range(1, 29):
                n13 = h1 - n11 - n12
                if n13 < 1:
                    continue
                n23 = h2 - n21 - n22
                if n23 < 1:
                    continue
                n31 = w1 - n11 - n21
                if n31 < 1:
                    continue
                n32 = w2 - n12 - n22
                if n32 < 1:
                    continue
                n33 = h3 - n31 - n32
                if n33 < 1:
                    continue
                if w3 == n13 + n23 + n33:
                    answer += 1

print(answer)
