def directory_size(directory: str, contents: dict):
    size = 0
    dir_contents = contents[directory]
    for item in dir_contents:
        if isinstance(item, int):
            size += item
        else:
            size += directory_size('/'.join([directory, item]), contents)
    return size


def day_7():
    with open('day7_input.txt') as f:
        current_path = []
        path_contents = {}
        while True:
            terminal_line = f.readline().strip().split()
            if not terminal_line:
                break
            if terminal_line[0] == '$':
                if terminal_line[1] == 'cd':
                    if terminal_line[2] != '..':
                        current_path.append(terminal_line[2])
                    else:
                        current_path.pop()
                if terminal_line[1] == 'ls':
                    continue
            else:
                current_dir = '/'.join(current_path)
                contents = path_contents.get(current_dir, [])
                if terminal_line[0] == 'dir':
                    contents.append(terminal_line[1])
                else:
                    contents.append(int(terminal_line[0]))
                path_contents[current_dir] = contents

    part_a_result = 0
    part_b_result = 0
    sizes = [directory_size(directory, path_contents) for directory in path_contents.keys()]
    required_space = 30000000 - (70000000 - sizes[0])
    sizes.sort(reverse=True)
    for size in sizes:
        if size <= 100000:
            part_a_result += size
        if size >= required_space:
            part_b_result = size
    return part_a_result, part_b_result


if __name__ == '__main__':
    result = day_7()
    print('Sum of directories smaller than 100k:', result[0])
    print('Smallest size to be deleted:', result[1])

