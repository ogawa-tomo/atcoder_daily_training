from collections import defaultdict

S = list(input())
T = list(input())

atcoder = ["a", "t", "c", "o", "d", "e", "r"]

s_dict: defaultdict[str, int] = defaultdict(int)
for s in S:
    s_dict[s] += 1
t_dict: defaultdict[str, int] = defaultdict(int)
for t in T:
    t_dict[t] += 1

# print(s_dict)
# print(t_dict)

for s in S:
    # print(s)
    # print(s_dict)
    # print(t_dict)
    if s == "@":
        # いったんあとまわし
        pass
    elif t_dict[s] > 0:
        t_dict[s] -= 1
        s_dict[s] -= 1
    elif s in atcoder and t_dict["@"] > 0:
        # tの@を使う
        t_dict["@"] -= 1
        s_dict[s] -= 1
    else:
        # sはatcoderではなく、tに対応する文字もない
        print("No")
        exit()

# この時点で、Sには"@"しか残っていない

# print("T")
# t側で割当たっていない文字について
for t in T:
    if t_dict[t] == 0:
        continue
    # print(t)
    # print(t_dict)
    # print(s_dict)
    if (t in atcoder or t == "@") and s_dict["@"] > 0:
        # atcoderか@であれば、sの@と対応させることができる
        t_dict[t] -= 1
        s_dict["@"] -= 1
    else:
        # 無理だったら、だめ
        print("No")
        exit()

print("Yes")
