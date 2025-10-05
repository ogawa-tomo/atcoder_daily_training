# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


N, K, X = map(int, input().split())
S: list[str] = []
for _ in range(N):
    s = input()
    S.append(s)

# print(S)

strings: list[str] = []


# N**K通りの文字列の列挙にdfsを用いる
def dfs(current_string, count):
    if count == K:
        strings.append(current_string)
        return
    for s in S:
        dfs(current_string + s, count + 1)


dfs("", 0)

strings.sort()
# print(strings)

print(strings[X - 1])
