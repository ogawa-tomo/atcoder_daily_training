S = list(input())
T = list(input())


def shift(char: str, distance: int):
    return chr((ord(char) + distance - 97) % 26 + 97)


# print(shift("a", 25))

for i in range(26):
    shifted_t = [shift(t, i) for t in T]
    if shifted_t == S:
        print("Yes")
        exit()
print("No")
