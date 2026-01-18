from collections import defaultdict

N, K, D = map(int, input().split())
A = list(map(int, input().split()))

# reminder_dict[i]: Dで割った余りがiであるようなAの要素のリスト
reminder_dict: defaultdict[int, list[int]] = defaultdict(list[int])

for a in A:
    reminder_dict[a % D].append(a)

reminder_dict2 = reminder_dict.copy()
reminder_dict2[0] = reminder_dict2[0].copy()
reminder_dict2[0].pop()
print(reminder_dict2)

print(reminder_dict)
