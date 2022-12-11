import math
import operator


def day_11(rounds:int, managed:bool):
    info = {}
    ops = {'+': operator.add, '*': operator.mul}
    monkey_count = {}
    test_ints = []

    # input parsing
    with open('day11_input.txt') as f:
        while True:
            note = f.readline().strip().split()
            if not note:
                break
            if note[0] == 'Monkey':
                monkey = int(note[1][0])
                info[monkey] = {}
                note = f.readline().strip().split(maxsplit=2)
                info[monkey]['items'] = [int(item) for item in note[2].split(', ')]
                note = f.readline().strip().split(sep=' = ')
                info[monkey]['operation'] = note[1].split()
                note = f.readline().strip().split()
                info[monkey]['test'] = int(note[-1])
                test_ints.append(int(note[-1]))
                info[monkey]['result'] = {}
                note = f.readline().strip()
                info[monkey]['result']['true'] = int(note[-1])
                note = f.readline().strip()
                info[monkey]['result']['false'] = int(note[-1])
                monkey_count[monkey] = 0
                f.readline()

    lcm = math.lcm(*test_ints)
    for round in range(rounds):
        for monkey in info.keys():
            monkey_info = info[monkey]
            items = monkey_info['items']
            for item in items:
                operation = monkey_info['operation']
                value = ops[operation[1]](int(operation[0].replace('old', str(item))), int(operation[2].replace('old', str(item))))
                if managed:
                    value = math.floor(value / 3)
                if value > lcm:
                    value %= lcm
                if value % monkey_info['test'] == 0:
                    info[monkey_info['result']['true']]['items'].append(value)
                else:
                    info[monkey_info['result']['false']]['items'].append(value)
                monkey_count[monkey] += 1
            info[monkey]['items'] = []

    inspections = [i for i in monkey_count.values()]
    inspections.sort(reverse=True)
    monkey_business = inspections[0] * inspections[1]
    return monkey_business


if __name__ == '__main__':
    print('i) Monkey business:', day_11(20, True))
    print('ii) Monkey business:', day_11(10000, False))
