N = int(input())
P = list(map(int, input().split()))

# joy[n]: n回回したときの嬉しさ
joy = [0] * N
for i in range(N):
    p = P[i]
    # この料理で喜ぶのは人pしかいない。なので、この料理が人pの前か前後に来るときに嬉しさが発生する
    joy[(p - i) % N] += 1
    joy[(p + 1 - i) % N] += 1
    joy[(p - 1 - i) % N] += 1

print(max(joy))
