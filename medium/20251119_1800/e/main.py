N_, T_ = input().split()
N = int(N_)
T = list(T_)

len_t = len(T)

answers: list[int] = []
for i in range(N):
    S = list(input())
    len_s = len(S)

    if len_s == len_t:
        # 同じか、1文字入れ替え
        count = 0
        ok = True
        for j in range(len_t):
            s = S[j]
            t = T[j]
            if s != t:
                count += 1
                if count > 1:
                    ok = False
                    break
        if ok:
            answers.append(i + 1)

    elif len_s + 1 == len_t:
        # 挿入
        count = 0
        ok = True
        for j in range(len_s):
            s = S[j]
            t = T[j + count]
            if s != t:
                count += 1
                if count > 1:
                    ok = False
                    break
                if s != T[j + count]:
                    ok = False
                    break
        if ok:
            answers.append(i + 1)

    elif len_s - 1 == len_t:
        # 削除
        count = 0
        ok = True
        for j in range(len_t):
            s = S[j + count]
            t = T[j]
            if s != t:
                count += 1
                if count > 1:
                    ok = False
                    break
                if S[j + count] != t:
                    ok = False
                    break
        if ok:
            answers.append(i + 1)

print(len(answers))
print(*answers)
