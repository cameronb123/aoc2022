from itertools import cycle


def check_overlap(rock_row: list, grid_row: list) -> bool:
    return any([rock_row[i] == '#' and grid_row[i] == '#' for i in range(7)])


def day_17():
    with open('day17_input.txt') as f:
        jet_input = f.readline().strip()

    jet = cycle(jet_input)

    rocks = cycle([
        [['#', '#', '#', '#']],
        [['.', '#', '.'], ['#', '#', '#'], ['.', '#', '.']],
        [['#', '#', '#'], ['.', '.', '#'], ['.', '.', '#']],
        [['#'], ['#'], ['#'], ['#']],
        [['#', '#'], ['#', '#']]
    ])

    rock_count = 0
    height = 0
    grid = [['#'] * 7]
    grid.extend([['.'] * 7] * 3)
    while rock_count <= 2022:
        rock = next(rocks)
        print(rock)
        x = 2
        for i in range(4):
            # Rock movement until rest
            direction = next(jet)
            if direction == '<':
                x = max(x-1, 0)
            else:
                x = min(x+1, 7-len(rock[0]))

        y = -1
        while True:
            # Check direction move
            direction = next(jet)
            rock_grid = [['.'] * 7] * len(rock)
            if direction == '<':
                x = max(x - 1, 0)
                for i in range(len(rock)):
                    rock_grid[i][x - 1: x - 1 + len(rock[i])] = rock[i]
            else:
                x = min(x + 1, 7 - len(rock[0]))
                for i in range(len(rock)):
                    rock_grid[i][x + 1: x + 1 + len(rock[i])] = rock[i]

            rock_rows = rock_grid[:min(3, abs(y))]
            grid_rows = grid[y:]
            if any([check_overlap(rock_rows[i], grid_rows[i]) for i in range(len(rock_rows))]):

                break

            # Check down move
            y -= 1
            rock_rows = rock_grid[:min(3, abs(y))]
            grid_rows = grid[:y]
            if any([check_overlap(rock_rows[i], grid_rows[i]) for i in range(len(rock_rows))]):
                break

        z = len(rock) - abs(y)

        for i in range(z):
            for j in range(7):
                if grid[y-i][j] == '#' or rock_grid[i][j] == '#':
                    grid[y-i][j] = '#'
                else:
                    grid[y-i][j] = '.'
        grid.extend(rock_rows[])
        rock_count += 1

    print(height)


if __name__ == '__main__':
    day_17()
