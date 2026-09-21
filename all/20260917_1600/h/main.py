from typing import Union
import sys

sys.setrecursionlimit(10**9)


class Node:
    def __init__(self) -> None:
        self.parent: Union[None, Node] = None
        self.size = 1
        self.is_black = False
        self.black_num = 0

    @property
    def root(self):
        if self.parent is None:
            return self
        return self.parent.root

    def switch_color(self):
        if self.is_black:
            self.is_black = False
            self.root.black_num -= 1
        else:
            self.is_black = True
            self.root.black_num += 1

    @property
    def can_reach_black(self):
        return self.root.black_num > 0


def is_same(node1: Node, node2: Node):
    return node1.root == node2.root


def unite(node1: Node, node2: Node):
    root1 = node1.root
    root2 = node2.root
    if root1 == root2:
        raise
    if root1.size < root2.size:
        root1.parent = root2
        root2.size += root1.size
        root2.black_num += root1.black_num
    else:
        root2.parent = root1
        root1.size += root2.size
        root1.black_num += root2.black_num


N, Q = map(int, input().split())

nodes = [Node() for _ in range(N)]
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        u = q[1]
        v = q[2]
        u -= 1
        v -= 1
        node_u = nodes[u]
        node_v = nodes[v]
        if not is_same(node_u, node_v):
            unite(node_u, node_v)
    elif q[0] == 2:
        v = q[1]
        v -= 1
        node_v = nodes[v]
        node_v.switch_color()

    elif q[0] == 3:
        v = q[1]
        v -= 1
        node_v = nodes[v]
        if node_v.can_reach_black:
            print("Yes")
        else:
            print("No")
