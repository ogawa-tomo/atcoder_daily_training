# TLE
from collections import defaultdict


class Cookie:
    def __init__(self, i: int, j: int, color: str):
        self.i = i
        self.j = j
        self.color = color

    def __repr__(self):
        return self.color


alphabets = "abcdefghijklmnopqrstuvwxyz"

H, W = map(int, input().split())
cookies: list[list[Cookie]] = []
for i in range(H):
    cookie_row: list[Cookie] = []
    row_data = list(input())
    for j in range(W):
        data = row_data[j]
        cookie = Cookie(i, j, data)
        cookie_row.append(cookie)
    cookies.append(cookie_row)


class CookiesManager:
    def __init__(self, cookies: list[list[Cookie]]):
        self.cookies = cookies

        # row[i]["a"]: i行目のaの数
        self.row: list[defaultdict[str, int]] = []
        for _ in range(H):
            self.row.append(defaultdict(int))

        self.column: list[defaultdict[str, int]] = []
        for _ in range(W):
            self.column.append(defaultdict(int))

        for i in range(H):
            for j in range(W):
                s = cookies[i][j].color
                self.row[i][s] += 1
                self.column[j][s] += 1

        # deleted_row_num["a"]: aで消された行の数
        self.deleted_row_num: defaultdict[str, int] = defaultdict(int)
        self.deleted_column_num: defaultdict[str, int] = defaultdict(int)

        self.deleted_rows: set[int] = set()
        self.deleted_columns: set[int] = set()

        self.deleted_count = 0

    def row_num(self):
        return H - len(self.deleted_rows)

    def column_num(self):
        return W - len(self.deleted_columns)

    def row_meets_condition(self, i: int) -> str:
        if i in self.deleted_rows:
            return ""
        if self.column_num() <= 1:
            return ""
        for s in alphabets:
            if self.row[i][s] == self.column_num() + self.deleted_column_num[s]:
                return s
        return ""

    def column_meets_condition(self, j: int) -> str:
        if j in self.deleted_columns:
            return ""
        if self.row_num() <= 1:
            return ""
        for s in alphabets:
            if self.column[j][s] == self.row_num() + self.deleted_row_num[s]:
                return s
        return ""

    def delete_row(self, i: int, s: str):
        self.deleted_count += self.column_num()
        self.deleted_row_num[s] += 1
        self.deleted_rows.add(i)

    def delete_column(self, j: int, s: str):
        self.deleted_count += self.row_num()
        self.deleted_column_num[s] += 1
        self.deleted_columns.add(j)


cookies_manager = CookiesManager(cookies)
while True:
    deleted = False
    delete_rows: list[tuple[int, str]] = []
    for i in range(H):
        # チェック
        s = cookies_manager.row_meets_condition(i)
        if s:
            delete_rows.append((i, s))
            # cookies_manager.delete_row(i, s)
            # deleted = True

    delete_columns: list[tuple[int, str]] = []
    for j in range(W):
        t = cookies_manager.column_meets_condition(j)
        if t:
            delete_columns.append((j, t))
            # cookies_manager.delete_column(j, t)
            # deleted = True

    if delete_rows or delete_columns:
        for delete_row in delete_rows:
            i = delete_row[0]
            s = delete_row[1]
            cookies_manager.delete_row(i, s)
        for delete_column in delete_columns:
            j = delete_column[0]
            t = delete_column[1]
            cookies_manager.delete_column(j, t)
        continue
    break

# print(cookies_manager.deleted_rows)
print(H * W - cookies_manager.deleted_count)
