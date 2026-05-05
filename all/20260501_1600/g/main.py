# あきらめた
import sys


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []
        self.koma: Koma | None = None
        self.visited = False

    def is_ok(self):
        if self.i == 8:
            return True
        return self.koma is not None and self.koma.i == self.i

    def __repr__(self):
        return str(self.i)


class Koma:
    def __init__(self, i: int, node: Node) -> None:
        self.node = node
        self.i = i


M = int(input())
nodes: list[Node] = [Node(i) for i in range(9)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)

P = list(map(int, input().split()))
komas: list[Koma] = []
for i, p in enumerate(P):
    node = nodes[p - 1]
    koma = Koma(i, node)
    komas.append(koma)
    node.koma = koma


# 空きノードを含む連結成分を取り出す
empty_node: Node | None = None
for node in nodes:
    if node.koma is None:
        empty_node = node
        break
if empty_node is None:
    raise
nodes_with_empty: set[Node] = set()


def dfs1(node: Node):
    node.visited = True
    nodes_with_empty.add(node)
    for to_node in node.to_nodes:
        if not to_node.visited:
            dfs1(to_node)


dfs1(empty_node)

print(nodes_with_empty)


# その連結成分以外のノードをチェック
for node in nodes:
    if node in nodes_with_empty:
        continue
    if not node.is_ok():
        print(-1)
        exit()

print("hoge")


def is_ok():
    for node in nodes_with_empty:
        if not node.is_ok():
            return False
    return True


def to_tuple():
    ll: list[int] = []
    for node in nodes_with_empty:
        if node.koma is None:
            continue
        ll.append(node.i)
    return tuple(ll)


# 空きノードを含む連結成分について、再帰的にコマを動かす
class Move:
    def __init__(self) -> None:
        self.answer = sys.maxsize
        self.emerged: set[tuple[int, ...]] = set()

    def move(self, count: int, last_moved_node: Node | None):
        if is_ok():
            self.answer = min(self.answer, count)
            return
        t = to_tuple()
        if t in self.emerged:
            return
        self.emerged.add(t)
        for node in nodes_with_empty:
            if node == last_moved_node:
                continue
            self.move(count + 1, node)


move = Move()
move.move(0, None)
if move.answer == sys.maxsize:
    print(-1)
else:
    print(move.answer)
