# TLE


def f(k):
    if k == 0:
        return 1
    if k == 1:
        return 2
    if k == 2:
        return 3
    # if k >= 3:
    return f((k // 2) // 2) + 2 * f((k // 2) // 3) + f((k // 3) // 3)

    # return f(k // 2) + f(k // 3)


N = int(input())

print(f(N))
