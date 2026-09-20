A, B, C, D = map(int, input().split())
C -= 1
D -= 1


# leftからrightの範囲で、modでrem余るマスの数
def num(left: int, right: int, mod: int, rem: int):
    if left % mod == rem:
        next_left = left
    elif left % mod > rem:
        next_left = (left + mod) - (left % mod) + rem
    else:
        next_left = left + (rem - left % mod)

    if next_left <= right:
        return ((right - next_left) // mod) + 1
    else:
        return 0


# 面積2
# x % 4 == 0 and y % 2 == 0の数
num_2_1 = num(A, C, 4, 0)
num_2_1 *= num(B, D, 2, 0)

# x % 4 == 1 and y % 2 == 1の数
num_2_2 = num(A, C, 4, 1)
num_2_2 *= num(B, D, 2, 1)

num_2 = num_2_1 + num_2_2

# 面積1
# x % 2 == 0 and y % 2 == 1の数
num_1_1 = num(A, C, 2, 0)
num_1_1 *= num(B, D, 2, 1)
# x % 2 == 1 and y % 2 == 0の数
num_1_2 = num(A, C, 2, 1)
num_1_2 *= num(B, D, 2, 0)

num_1 = num_1_1 + num_1_2

print(2 * num_2 + num_1)
