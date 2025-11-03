A, M, L, R = map(int, input().split())


if (R - A) % M == 0 or (L - A) % M == 0:
    print((R - L) // M + 1)
    exit()


# AとRの間の木（Aを含まない）
AR = abs(R - A) // M

# AとLの間の木（Aを含まない）
AL = abs(L - A) // M

if A < L or R < A:
    print(abs(AR - AL))
else:
    print(AR + AL + 1)
