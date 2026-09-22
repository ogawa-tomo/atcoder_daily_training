N, K = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
total_by_num: dict[int, int] = {}
for a in A:
    if a in total_by_num:
        total_by_num[a] += a
    else:
        total_by_num[a] = a

# print(total_by_num)
total_by_num_list = [total_by_num[x] for x in total_by_num]
# print(total_by_num_list)
total_by_num_list.sort(reverse=True)

for k in range(K):
    if k > len(total_by_num_list) - 1:
        break
    total -= total_by_num_list[k]

print(total)
