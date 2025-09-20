S = list(input())


def is_palindrome(string: list[str]):
    length = len(string)
    for i in range(len(string) // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True


answer = 0
length = len(S)
for i in range(length + 1):
    for j in range(i + 1, length + 1):
        string = S[i:j]
        # print(string)
        if is_palindrome(string):
            answer = max(answer, len(string))

print(answer)
