def day14():
    grid = {}
    with open('day14_input.txt') as f:
        while True:
            path = f.readline()
            if not path:
                break
            else:
                path = path.strip().split(' -> ')

            for i in range(len(path) - 1):
                start = path[i].split(',')
                end = path[i+1].split(',')

                if start[0] == end[0]:
                    col = grid.setdefault(int(start[0]), [])
                    a, b = min(int(start[1]), int(end[1])), max(int(start[1]), int(end[1]))
                    col.extend([j for j in range(a, b+1)])
                    grid[int(start[0])] = col
                else:
                    a, b = min(int(start[0]), int(end[0])), max(int(start[0]), int(end[0]))
                    for j in range(a, b+1):
                        row = grid.setdefault(j, [])
                        row.append(int(start[1]))
                        grid[j] = row

    floor = max([max(col) for col in grid.values()]) + 2

    sand_units = 0
    sand = [500, 0]
    while True:
        if sand[1] + 1 not in grid.get(sand[0], []) and sand[1] + 1 < floor:
            sand[1] += 1
        elif sand[1] + 1 not in grid.get(sand[0] - 1, []) and sand[1] + 1 < floor:
            sand = [sand[0] - 1, sand[1] + 1]
        elif sand[1] + 1 not in grid.get(sand[0] + 1, []) and sand[1] + 1 < floor:
            sand = [sand[0] + 1, sand[1] + 1]
        else:
            col = grid.setdefault(sand[0], [])
            col.append(sand[1])
            grid[sand[0]] = col
            sand_units += 1
            if sand == [500, 0]:
                break
            sand = [500, 0]
    return sand_units


if __name__ == '__main__':
    print('Sand units at rest:', day14())
