N = int(input())

unit: list[list[str]] = [["#"]]


def make(unit: list[list[str]], count: int):
    if count == N:
        return unit
    new_unit: list[list[str]] = []
    mod = 3**count
    for i in range(3 ** (count + 1)):
        row: list[str] = []
        for j in range(3 ** (count + 1)):
            if i // mod == 1 and j // mod == 1:
                row.append(".")
            else:
                ii = i % mod
                jj = j % mod
                row.append(unit[ii][jj])
        new_unit.append(row)
    return make(new_unit, count + 1)


answer = make(unit, 0)
for a in answer:
    print("".join(a))
