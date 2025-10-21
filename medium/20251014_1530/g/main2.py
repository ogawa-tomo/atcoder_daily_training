N = int(input())
T = list(map(int, list(input())))

# print(T)

# 0が偶数個なら美しい
# なぜならば、操作によって0の偶奇は変わらないから（不変量）

# 0を奇数個含み、現在のインデックスで終わる文字列の数
odd_zero = 0
# 0を偶数個含み、現在のインデックスで終わる文字列の数
even_zero = 0

answer = 0
for t in T:
    if t == 0:
        # 既存の文字列は偶奇が反転する
        current_odd_zero = odd_zero
        odd_zero = even_zero
        even_zero = current_odd_zero
        # 0だけの文字列が追加される
        odd_zero += 1
    else:
        # 1だけの文字列が追加される
        even_zero += 1

    # 0が偶数個の文字列を数える
    answer += even_zero


print(answer)
