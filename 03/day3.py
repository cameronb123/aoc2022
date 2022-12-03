from string import ascii_letters


def day_3_a():
    priority_score = 0
    with open('day3_input.txt') as f:
        while True:
            rucksack = f.readline().strip()
            if not rucksack:
                break
            rucksack_size = len(rucksack)
            compartment_1 = rucksack[:int(rucksack_size / 2)]
            compartment_2 = rucksack[int(rucksack_size / 2):]
            overlap = [item for item in set(compartment_1) if item in set(compartment_2)]
            for item in overlap:
                priority_score += ascii_letters.index(item) + 1
    return priority_score


def day_3_b():
    priority_score = 0
    with open('day3_input.txt') as f:
        while True:
            rucksack = [f.readline().strip() for i in range(3)]
            if not rucksack[0]:
                break
            overlap = [item for item in set(rucksack[0]) if item in set(rucksack[1]) and item in set(rucksack[2])]
            priority_score += ascii_letters.index(overlap[0]) + 1
    return priority_score


if __name__ == '__main__':
    print('Item priority sum:', day_3_a())
    print('Group priority sum:', day_3_b())

