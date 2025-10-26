from collections import deque


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.color: str | None = None  # "black" or "white"
        self.to_nodes: list[Node] = []
        self.to_nodes_num = 0
        self.renketsu: Renketsu | None = None


class Renketsu:
    def __init__(self):
        self.black_num = 0
        self.white_num = 0

    def total_num(self):
        return self.black_num + self.white_num


N, M = map(int, input().split())

nodes = [Node(i) for i in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_u.to_nodes_num += 1
    node_v.to_nodes.append(node_u)
    node_v.to_nodes_num += 1

# 連結成分に分解
# それぞれの連結成分について、色を塗って2部グラフであるかを判定
# また、連結成分ごとに、黒の数と白の数を保持する
d: deque[Node] = deque()
for node in nodes:
    d.append(node)
while d:
    start_node = d.popleft()
    if start_node.color is not None:
        continue
    # 色のついていないノードがあれば、それについて連結成分を作成し、色をつけていく
    renketsu = Renketsu()
    dd: deque[Node] = deque()
    dd.append(start_node)
    start_node.color = "black"
    while dd:
        node = dd.popleft()
        node.renketsu = renketsu
        if node.color == "black":
            renketsu.black_num += 1
        else:
            renketsu.white_num += 1
        for to_node in node.to_nodes:
            if to_node.color == node.color:
                # 2部グラフではないのでNG
                print(0)
                exit()
            if to_node.color is None:
                if node.color == "black":
                    to_node.color = "white"
                else:
                    to_node.color = "black"
                dd.append(to_node)

# それぞれのノードについて、以下の数を答えに足す
# 自分の連結成分の自分と異なる色の数 - 自分から出ているリンクの数
# 自分の連結成分以外のノードの数
answer = 0
for node in nodes:
    if node.renketsu is None:
        raise
    renketsu = node.renketsu
    if node.color == "black":
        answer += renketsu.white_num - node.to_nodes_num
    elif node.color == "white":
        answer += renketsu.black_num - node.to_nodes_num
    answer += N - renketsu.total_num()

# 2で割っておわり
answer //= 2
print(answer)
