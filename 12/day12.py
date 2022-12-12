from string import ascii_lowercase


def day_12(all_starts: bool = False):
    with open('day12_input.txt') as f:
        grid = f.readlines()

    s_loc = e_loc = [0, 0]
    locations = []
    for line in grid:
        line.strip()
        if 'S' in line:
            s_loc = [grid.index(line), line.index('S')]
            locations.append(s_loc)
            print('s_loc', s_loc)
        if 'E' in line:
            e_loc = [grid.index(line), line.index('E')]
            print('e_loc', e_loc)
        if all_starts:
            if 'a' in line:
                locations.extend([[grid.index(line), i] for i, x in enumerate(line) if x == 'a'])

    grid[e_loc[0]] = grid[e_loc[0]].replace('E', 'z')

    path_length = 0
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    m = len(grid)
    n = len(grid[0])
    while True:
        print(locations)
        path_length += 1
        new_locs = []
        for loc in locations:
            if loc != s_loc:
                letter = grid[loc[0]][loc[1]]
                letters = ascii_lowercase[:ascii_lowercase.index(letter)+2]
            else:
                letters = 'a'
            for move in moves:
                new_loc = [loc[i] + move[i] for i in range(2)]
                try:
                    new_letter = grid[new_loc[0]][new_loc[1]]
                    if (new_loc not in new_locs) and (0 <= new_loc[0] <= m) and (0 <= new_loc[1] <= n) and (new_letter in letters):
                        new_locs.append(new_loc)
                except IndexError:
                    continue
            if e_loc in new_locs:
                return path_length
        locations = new_locs


if __name__ == '__main__':
    print('Shortest path length:', day_12())
