def day_5():
    n = 9
    with open('day5_input.txt') as f:
        stacks = [[] for i in range(n)]
        line = f.readline()
        while line[:3] != ' 1 ':
            for i in range(n):
                letter = line[i * 4 + 1:i * 4 + 2].strip()
                if letter:
                    stacks[i].insert(0, letter)
            line = f.readline()
        f.readline()

        while True:
            moves = f.readline().strip().split()
            if not moves:
                break
            mover = stacks[int(moves[3]) - 1][-int(moves[1]):]
            stacks[int(moves[3]) - 1] = stacks[int(moves[3]) - 1][:-int(moves[1])]
            stacks[int(moves[5]) - 1].extend(mover)
    return ''.join([stack[-1] for stack in stacks])


if __name__ == '__main__':
    print('Rearrangement output:', day_5())
