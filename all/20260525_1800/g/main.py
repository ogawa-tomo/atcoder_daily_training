import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった


class Node:
    def __init__(self) -> None:
        self.links: list[Link] = []
        self.visited = False


class Link:
    def __init__(self, to_node: Node, weight: int) -> None:
        self.to_node = to_node
        self.weight = weight


N, M = map(int, input().split())
nodes: list[Node] = [Node() for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.links.append(Link(node_v, w))
    node_v.links.append(Link(node_u, w))


class Dfs:
    def __init__(self) -> None:
        self.answer = sys.maxsize

    def dfs(self, node: Node, current_weight: int):
        if node == nodes[N - 1]:
            self.answer = min(current_weight, self.answer)
            return
        node.visited = True
        for link in node.links:
            to_node = link.to_node
            if not to_node.visited:
                self.dfs(to_node, current_weight ^ link.weight)
                to_node.visited = False


dfs = Dfs()
dfs.dfs(nodes[0], 0)
print(dfs.answer)
