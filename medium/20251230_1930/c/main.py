W, B = map(int, input().split())

S = "wbwbwwbwbwbw" * 100


def match(string: str):
    if len(string) != W + B:
        return False

    w_count = 0
    b_count = 0
    for s in string:
        if s == "w":
            w_count += 1
        elif s == "b":
            b_count += 1

    return w_count == W and b_count == B


for i in range(len(S) - (W + B)):
    string = S[i : i + W + B]
    if match(string):
        print("Yes")
        exit()

print("No")
