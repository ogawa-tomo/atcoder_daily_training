N = int(input())


def is_palindrome(string: list[str]):
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True


strings: list[list[str]] = []
for _ in range(N):
    s = list(input())
    strings.append(s)
# print(strings)
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        string = [*strings[i], *strings[j]]
        # print(string)
        if is_palindrome(string):
            print("Yes")
            exit()

print("No")
