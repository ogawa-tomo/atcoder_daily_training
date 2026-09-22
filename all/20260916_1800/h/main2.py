# ギリギリTLE
from typing import Union
import sys

sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.value = 0
        self.to_links: list[Link] = []
        self.visited = False
        self.parent: Union[None, Node] = None
        self.size = 1

    @property
    def root(self):
        if self.parent is None:
            return self
        return self.parent.root

    def __repr__(self) -> str:
        return str(self.i + 1)


class Link:
    def __init__(self, to_node: Node, value: int) -> None:
        self.to_node = to_node
        self.value = value


def is_same(node1: Node, node2: Node):
    return node1.root == node2.root


def unite(node1: Node, node2: Node):
    if is_same(node1, node2):
        return
    root1 = node1.root
    root2 = node2.root
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
    else:
        root2.parent = root1
        root1.size += root2.size


N, M = map(int, input().split())
nodes = [Node(i) for i in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    node_x = nodes[x]
    node_y = nodes[y]
    node_x.to_links.append(Link(node_y, z))
    node_y.to_links.append(Link(node_x, z))
    unite(node_x, node_y)

roots: set[Node] = set()
for node in nodes:
    root = node.root
    if root not in roots:
        roots.add(root)


# nodeのdigit桁目にvalueを設定したときの合計
def dfs(node: Node, digit: int, value: int):
    count = value
    if value == 1:
        node.value |= 1 << digit  # digit桁目を1にする
    else:
        node.value &= ~(1 << digit)  # digit桁目を0にする
    node.visited = True
    for to_link in node.to_links:
        to_node = to_link.to_node
        to_link_value = (to_link.value >> digit) & 1
        next_value = to_link_value ^ value  # 繋がっているノードのdigit桁目の値
        if not to_node.visited:
            count += dfs(to_node, digit, next_value)
        else:
            if (to_node.value >> digit) & 1 != next_value:
                print(-1)
                exit()

    return count


connected_nodes_dict: dict[Node, list[Node]] = {}
for node in nodes:
    root = node.root
    if root in connected_nodes_dict:
        connected_nodes_dict[root].append(node)
    else:
        connected_nodes_dict[root] = [node]

for root in roots:
    # 各連結成分について
    connected_nodes = connected_nodes_dict[root]
    for digit in range(30):
        # 各桁について
        for node in connected_nodes:
            node.visited = False

        # rootの該当桁を0にしたとき、1になる数をカウント（ついでに矛盾がないかチェック）
        count = dfs(root, digit, 0)
        # もし、sizeの半分を超えていたら、リセットしてrootの該当行を1にする
        if count > root.size // 2:
            for node in connected_nodes:
                node.visited = False
            dfs(root, digit, 1)

print(*[n.value for n in nodes])
