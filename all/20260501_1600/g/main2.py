from collections import deque


class Node:
    def __init__(self, i: int) -> None:
        self.i = i
        self.to_nodes: list[Node] = []


M = int(input())
nodes: list[Node] = [Node(i) for i in range(9)]
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    node_u = nodes[u]
    node_v = nodes[v]
    node_u.to_nodes.append(node_v)
    node_v.to_nodes.append(node_u)

P = list(map(int, input().split()))

# state[i]: i個目のコマがいるノードのインデックス
init_state_list: list[int] = []
for p in P:
    init_state_list.append(p - 1)
init_state = "".join([str(s) for s in init_state_list])


# あるstateから遷移できるstate
def to_states(state: str):
    results: list[str] = []

    nodes_with_koma = [nodes[int(node_index_str)] for node_index_str in state]
    empty_node: Node | None = None
    for node in nodes:
        if node not in nodes_with_koma:
            empty_node = node
            break
    if empty_node is None:
        raise

    # それぞれのコマについて、いまいるノードが空きノードに繋がっていれば、コマを空きノードに移動させたstateに遷移できる
    for koma_index, node_index_str in enumerate(state):
        node = nodes[int(node_index_str)]
        if empty_node in node.to_nodes:
            new_state = list(state)
            new_state[koma_index] = str(empty_node.i)
            results.append("".join(new_state))
    return results


# state_distance[state]: 状態の距離
state_distance: dict[str, int] = {}

d: deque[str] = deque()
d.append(init_state)
state_distance[init_state] = 0
while d:
    state = d.popleft()
    distance = state_distance[state]
    for to_state in to_states(state):
        if to_state not in state_distance:
            d.append(to_state)
            state_distance[to_state] = distance + 1

if "01234567" in state_distance:
    print(state_distance["01234567"])
else:
    print(-1)
