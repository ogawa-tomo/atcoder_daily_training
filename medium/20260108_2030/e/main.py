N = int(input())
toys = list(map(int, input().split()))
boxes = list(map(int, input().split()))

toys.sort(reverse=True)
boxes.sort(reverse=True)

# print(boxes)

bought_box_size: None | int = None

for i in range(N - 1):
    if bought_box_size is None:
        toy = toys[i]
        box = boxes[i]
        if box >= toy:
            continue
        else:
            bought_box_size = toy
            toy = toys[i + 1]
            if toy > box:
                print(-1)
                exit()
    else:
        toy = toys[i + 1]
        box = boxes[i]
        if box >= toy:
            continue
        else:
            print(-1)
            exit()

if bought_box_size is None:
    print(toys[-1])
else:
    print(bought_box_size)
