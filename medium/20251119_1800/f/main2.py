N = int(input())
H = list(map(int, input().split()))

T = 0
for h in H:
    three_turns = h // 5
    T += three_turns * 3
    h -= three_turns * 5
    while h > 0:
        T += 1
        if T % 3 == 0:
            h -= 3
        else:
            h -= 1

print(T)
