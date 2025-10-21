N = int(input())
T = list(map(int, list(input())))

# print(T)

# 文字列の長さが偶数のとき、1が偶数個あれば美しい
# 文字列の長さが奇数のとき、1が奇数個あれば美しい

# 奇数インデックスから始まり、1が奇数個あり、現在のインデックスで終わる文字列の数
starts_odd_one_odd = 0
# 奇数インデックスから始まり、1が偶数個あり、現在のインデックスで終わる文字列の数
starts_odd_one_even = 0
# 偶数インデックスから始まり、1が奇数個あり、現在のインデックスで終わる文字列の数
starts_even_one_odd = 0
# 偶数インデックスから始まり、1が偶数個あり、現在のインデックスで終わる文字列の数
starts_even_one_even = 0

answer = 0
for i, t in enumerate(T):
    current_even = (i + 1) % 2 == 0
    if t == 1:
        # 既存の文字列は偶奇が反転する
        tmp = starts_odd_one_even
        starts_odd_one_even = starts_odd_one_odd
        starts_odd_one_odd = tmp
        tmp = starts_even_one_even
        starts_even_one_even = starts_even_one_odd
        starts_even_one_odd = tmp

        # 1だけの文字列が追加される
        if current_even:
            starts_even_one_odd += 1
        else:
            starts_odd_one_odd += 1
    else:
        # 0だけの文字列が追加される
        if current_even:
            starts_even_one_even += 1
        else:
            starts_odd_one_even += 1

    if current_even:
        # 長さが奇数の文字列
        answer += starts_even_one_odd
        # 長さが偶数の文字列
        answer += starts_odd_one_even
    else:
        # 長さが奇数の文字列
        answer += starts_odd_one_odd
        # 長さが偶数の文字列
        answer += starts_even_one_even

print(answer)
