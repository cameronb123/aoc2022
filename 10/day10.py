def day_10():
    x = 1
    signal_strength_sum = 0
    cycle_number = 0
    pixel = 0
    cycle_breaks = (20, 60, 100, 140, 180, 220)
    crt = ''

    with open('day10_input.txt') as f:
        while True:
            command = f.readline().strip().split()
            if not command:
                break

            if command[0] == 'noop':
                cycles = 1
            else:
                cycles = 2

            for i in range(cycles):
                cycle_number += 1
                if cycle_number in cycle_breaks:
                    signal_strength = cycle_number * x
                    signal_strength_sum += signal_strength
                if x - 1 <= pixel <= x + 1:
                    crt += '#'
                else:
                    crt += '.'
                pixel += 1
                if pixel > 39:
                    pixel = 0

            if command[0] == 'addx':
                x += int(command[1])

    return signal_strength_sum, crt


if __name__ == '__main__':
    signal, crt = day_10()
    print('Signal strength sum:', signal)
    print('')
    for i in range(6):
        print(crt[40*i: 40*(i+1)])