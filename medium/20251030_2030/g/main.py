from collections import deque
import math


class User:
    def __init__(self, i: int):
        self.i = i
        self.friends: list[User] = []
        self.visited = False


# class Renketsu:
#     def __init__(self, i: int):
#         self.i = i
#         self.num = 0


N, M = map(int, input().split())
users = [User(i) for i in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    user_a = users[a]
    user_b = users[b]
    user_a.friends.append(user_b)
    user_b.friends.append(user_a)

renketsu_list: list[int] = []
for first_user in users:
    if first_user.visited:
        continue
    d: deque[User] = deque()
    d.append(first_user)
    first_user.visited = True
    renketsu_num = 0
    while d:
        user = d.popleft()
        renketsu_num += 1
        for friend in user.friends:
            if not friend.visited:
                friend.visited = True
                d.append(friend)
    renketsu_list.append(renketsu_num)

answer = 0
for renketsu_num in renketsu_list:
    answer += math.comb(renketsu_num, 2)
answer -= M
print(answer)
