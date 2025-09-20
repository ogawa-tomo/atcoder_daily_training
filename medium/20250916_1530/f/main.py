import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)


class Node:
    def __init__(self, number: int) -> None:
        self.number = number
        self.neighbors: list[Node] = []
        self.visited = False


nodes: dict[int, Node] = {}

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    if a not in nodes:
        nodes[a] = Node(a)
    if b not in nodes:
        nodes[b] = Node(b)
    node_a = nodes[a]
    node_b = nodes[b]
    node_a.neighbors.append(node_b)
    node_b.neighbors.append(node_a)


class DFS:
    def __init__(self, nodes: dict[int, Node]):
        self.answer = 1
        self.nodes = nodes

    def dfs(self, node: Node):
        node.visited = True
        self.answer = max(self.answer, node.number)
        for neighbor in node.neighbors:
            if not neighbor.visited:
                self.dfs(neighbor)


dfs = DFS(nodes)
if 1 in nodes:
    dfs.dfs(nodes[1])

print(dfs.answer)
