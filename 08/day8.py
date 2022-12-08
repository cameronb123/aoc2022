def day_8():
    grid = []
    visible_trees = 0
    max_scenic_score = 0
    with open('day8_input.txt') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            grid.append(line)
    m = len(grid[0])
    n = len(grid)

    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                visible_trees += 1
            else:
                tree = int(grid[i][j])
                paths = [[int(num) for num in grid[i][:j]],
                         [int(num) for num in grid[i][j + 1:]],
                         [int(grid[row][j]) for row in range(i)],
                         [int(grid[row][j]) for row in range(i + 1, m)]]
                paths[0].reverse()
                paths[2].reverse()
                for path in paths:
                    if all([tree > num for num in path]):
                        visible_trees += 1
                        break

                tree_scenic_score = 1
                for path in paths:
                    path_scenic_score = 0
                    for num in path:
                        path_scenic_score += 1
                        if num >= tree:
                            break
                    tree_scenic_score *= path_scenic_score
                max_scenic_score = max(max_scenic_score, tree_scenic_score)

    return visible_trees, max_scenic_score


if __name__ == '__main__':
    result = day_8()
    print('Visible trees:', result[0])
    print('Max scenic score:', result[1])
