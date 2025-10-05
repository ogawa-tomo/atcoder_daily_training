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

current_node: Node | None = None
for node in nodes:
    if len(node.neighbors) == 1:
        current_node = node
        break
if current_node is None:
    print("No")
    exit()

current_node.visited = True
for _ in range(M):
    if len(current_node.neighbors) > 2:
        print("No")
        exit()
    next_node_exists = False
    for neighbor in current_node.neighbors:
        if not neighbor.visited:
            current_node = neighbor
            current_node.visited = True
            next_node_exists = True
            break
    if not next_node_exists:
        print("No")
        exit()
print("Yes")
