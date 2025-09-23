from collections import deque

S = list(input())

stack: deque[str] = deque()

for s in S:
    if s == "(" or s == "[" or s == "<":
        stack.append(s)
    if s == ")":
        if not stack or stack.pop() != "(":
            print("No")
            exit()
    if s == "]":
        if not stack or stack.pop() != "[":
            print("No")
            exit()
    if s == ">":
        if not stack or stack.pop() != "<":
            print("No")
            exit()

if stack:
    print("No")
else:
    print("Yes")
