def day_1():
    current_elf_calories = 0
    top_3_elf_calories = [0, 0, 0]
    with open('day1_input.txt') as f:
        while True:
            input_value = f.readline()
            if not input_value:
                break
            input_value = input_value.strip()
            if input_value == '':
                if current_elf_calories > top_3_elf_calories[0]:
                    top_3_elf_calories[0] = current_elf_calories
                    top_3_elf_calories.sort()
                current_elf_calories = 0
            else:
                current_elf_calories += int(input_value)
    print('Top 3 elf calories: ', top_3_elf_calories)
    print('Sum of max elf calories: ', sum(top_3_elf_calories))


if __name__ == '__main__':
    day_1()