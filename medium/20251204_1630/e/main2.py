H, W, N = map(int, input().split())


existing_rows: list[int] = []
existing_columns: list[int] = []

for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    existing_rows.append(a)
    existing_columns.append(b)


# 座標圧縮
def compress_coord(org: list[int]):
    s = sorted(list(set(org)))
    rank: dict[int, int] = {}
    for i, x in enumerate(s):
        rank[x] = i
    return [rank[elem] for elem in org]


compressed_rows = compress_coord(existing_rows)
compressed_columns = compress_coord(existing_columns)
for i in range(N):
    row = compressed_rows[i]
    column = compressed_columns[i]
    print(row + 1, column + 1)
