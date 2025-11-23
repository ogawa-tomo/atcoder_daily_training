def GCD(A: int, B: int):

    while A > 0 and B > 0:
        if A > B:
            A = A % B
        else:
            B = B % A

    if A == 0:
        return B
    else:
        return A


def LCM(A: int, B: int):
    return A * int(B / GCD(A, B))


N, A, B = map(int, input().split())

lcm = LCM(A, B)
lcm_num = N // lcm
lcm_sum = (1 + lcm_num) * lcm_num * lcm // 2
a_num = N // A
a_sum = (1 + a_num) * a_num * A // 2
b_num = N // B
b_sum = (1 + b_num) * b_num * B // 2

total = (N + 1) * N // 2

print(total - a_sum - b_sum + lcm_sum)
