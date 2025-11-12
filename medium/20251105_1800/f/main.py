N = int(input())
S = list(input())

# "first": 最初の11..
# "slash": /が出ている
# "second": 次の22...
# "none": 不正状態
mode = "none"
answer = 0
if "/" in S:
    answer = 1
one_count = 0
two_count = 0
for s in S:
    if mode == "first":
        if s == "1":
            one_count += 1
        elif s == "/":
            mode = "slash"
        elif s == "2":
            mode = "none"
    elif mode == "slash":
        if s == "1":
            one_count = 1
            mode = "first"
        elif s == "/":
            mode = "none"
        elif s == "2":
            mode = "second"
            two_count = 1
    elif mode == "second":
        if s == "1":
            answer = max(answer, two_count * 2 + 1)
            mode = "first"
            one_count = 1
        elif s == "/":
            answer = max(answer, two_count * 2 + 1)
            mode = "none"
        elif s == "2":
            if two_count == one_count:
                answer = max(answer, one_count + two_count + 1)
                mode = "none"
            else:
                two_count += 1
    elif mode == "none":
        if s == "1":
            mode = "first"
            one_count = 1
        elif s == "/":
            pass
        elif s == "2":
            pass

if mode == "second":
    answer = max(answer, two_count * 2 + 1)
print(answer)
