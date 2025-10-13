import sys

sys.setrecursionlimit(10**9)  # 10^9が限界らしく、10^10にするとREになっちゃった

N = int(input())


class Node:
    def __init__(self, i) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.visited = 0


nodes = [Node(i) for i in range(N)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)


# nodeを消すのに必要な回数
def erase_count(node: Node):
    node.visited = True
    count = 0
    for to_node in node.to_nodes:
        if to_node.visited:
            continue
        count += erase_count(to_node)
    return count + 1


node_0 = nodes[0]
node_0.visited = True
answer = 0
max_count = 0  # 1に隣接するノードのうち、消すまでに最も回数のかかるノードのカウント
for node in node_0.to_nodes:
    count = erase_count(node)
    # print(count)
    max_count = max(max_count, count)
    answer += count

answer -= max_count  # 最も回数のかかるノードは消さなくていい
answer += 1  # 1を消す
print(answer)
