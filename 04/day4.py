def day_4():
    full_overlap_count = 0
    partial_overlap_count = 0
    with open('day4_input.txt') as f:
        while True:
            sections = f.readline()
            if not sections:
                break
            else:
                sections = [[int(i) for i in section.split('-')] for section in sections.strip().split(',')]
            if (sections[0][0] <= sections[1][0] and sections[0][1] >= sections[1][1])\
                    or (sections[1][0] <= sections[0][0] and sections[1][1] >= sections[0][1]):
                full_overlap_count += 1
                partial_overlap_count += 1
            elif (sections[0][0] <= sections[1][0] <= sections[0][1])\
                    or (sections[1][0] <= sections[0][0] <= sections[1][1]):
                partial_overlap_count += 1
    return full_overlap_count, partial_overlap_count


if __name__ == '__main__':
    result = day_4()
    print('Total full overlaps:', result[0])
    print('Total partial overlaps:', result[1])
