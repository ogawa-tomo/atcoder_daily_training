# 再帰関数を使う問題はPyPyだとTLEになることがあるので注意！CPythonにしたほうがよい。
import sys

# 再帰呼び出しの深さの上限を深くする
sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self) -> None:
        self.neighbors: list[Node] = []
        self.visited = False


N, M = map(int, input().split())

if M != N - 1:
    print("No")
    exit()

nodes: list[Node] = [Node() for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    nodes[u].neighbors.append(nodes[v])
    nodes[v].neighbors.append(nodes[u])

for node in nodes:
    if len(node.neighbors) > 2:
        print("No")
        exit()


def dfs(node: Node):
    node.visited = True
    for neighbor in node.neighbors:
        if not neighbor.visited:
            dfs(neighbor)


dfs(nodes[0])
for node in nodes:
    if not node.visited:
        print("No")
        exit()
print("Yes")
