def is_palindrome(string: list[str]):
    length = len(string)
    for i in range(len(string) // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True


S = list(input())
tail_a_num = 0
for s in S:
    if s == "a":
        tail_a_num += 1
    else:
        break
S.reverse()
head_a_num = 0
for s in S:
    if s == "a":
        head_a_num += 1
    else:
        break

if tail_a_num > head_a_num:
    print("No")
    exit()
for _ in range(head_a_num - tail_a_num):
    S.append("a")

if is_palindrome(S):
    print("Yes")
else:
    print("No")
