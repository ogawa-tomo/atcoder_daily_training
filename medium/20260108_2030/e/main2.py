N = int(input())
toys = list(map(int, input().split()))
boxes = list(map(int, input().split()))

toys.sort(reverse=True)
boxes.sort(reverse=True)

# print(boxes)

bought_box_size: None | int = None

toy_i = 0
box_i = 0
while box_i < N - 1:
    toy = toys[toy_i]
    box = boxes[box_i]

    if toy > box:
        if toy_i > box_i:
            print(-1)
            exit()
        bought_box_size = toy
        toy_i += 1
    else:
        toy_i += 1
        box_i += 1

if bought_box_size is None:
    print(toys[-1])
else:
    print(bought_box_size)
