from collections import defaultdict

N = int(input())

use_dict: defaultdict[int, bool] = defaultdict(bool)
use_dict[0] = True
while True:
    for i in range(1, 2 * N + 2):
        if not use_dict[i]:
            print(i, flush=True)
            use_dict[i] = True
            break

    t = int(input())
    if t == 0:
        exit()
    use_dict[t] = True
