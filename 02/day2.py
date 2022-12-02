def day_2_a():
    choice_map = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    choice_score = {'A': 1, 'B': 2, 'C': 3}
    win_map = {'A': 'C', 'B': 'A', 'C': 'B'}
    my_score = 0
    with open('day2_input.txt') as f:
        while True:
            rps_round = f.readline()
            if not rps_round:
                break
            rps_round = rps_round.strip().split()
            my_score += choice_score[choice_map[rps_round[1]]]
            if rps_round[0] == choice_map[rps_round[1]]:
                # Draw
                my_score += 3
            elif rps_round[0] == win_map[choice_map[rps_round[1]]]:
                # Win
                my_score += 6
    return my_score


def day_2_b():
    result_score = {'X': 0, 'Y': 3, 'Z': 6}
    choice_score = {'A': 1, 'B': 2, 'C': 3}
    loss_map = {'A': 'C', 'B': 'A', 'C': 'B'}
    win_map = {'A': 'B', 'B': 'C', 'C': 'A'}
    my_score = 0
    with open('day2_input.txt') as f:
        while True:
            rps_round = f.readline()
            if not rps_round:
                break
            rps_round = rps_round.strip().split()
            my_score += result_score[rps_round[1]]
            if rps_round[1] == 'Y':
                # Draw
                my_score += choice_score[rps_round[0]]
            elif rps_round[1] == 'Z':
                # Win
                my_score += choice_score[win_map[rps_round[0]]]
            else:
                # Loss
                my_score += choice_score[loss_map[rps_round[0]]]
    return my_score


if __name__ == '__main__':
    print('Total score a:', day_2_a())
    print('Total score b:', day_2_b())
