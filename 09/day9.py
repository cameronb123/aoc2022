from typing import List


def calculate_move(head: List, tail: List):
    if abs(head[0] - tail[0]) > 1:
        tail[0] = int((head[0] + tail[0]) / 2)
        if abs(tail[1] - head[1]) <= 1:
            tail[1] = head[1]
        else:
            tail[1] = int((head[1] + tail[1]) / 2)
    elif abs(head[1] - tail[1]) > 1:
        tail[1] = int((head[1] + tail[1]) / 2)
        if abs(tail[0] - head[0]) <= 1:
            tail[0] = head[0]
        else:
            tail[0] = int((head[0] + tail[0]) / 2)
    return tail


def day_9():
    knots = [[0, 0] for i in range(10)]
    move_dict = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
    tail_path = set()
    with open('day9_input.txt') as f:
        while True:
            move = f.readline().strip().split()
            if not move:
                break
            direction = move[0]
            for i in range(int(move[1])):
                knots[0] = [knots[0][j] + move_dict[direction][j] for j in range(2)]
                for i in range(1, 10):
                    knots[i] = calculate_move(knots[i - 1], knots[i])
                tail_path.add(tuple(knots[-1]))
    return len(tail_path)


if __name__ == '__main__':
    print('Tail positions:', day_9())
