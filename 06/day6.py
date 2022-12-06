def day_6():
    start_locations = []
    with open('day6_input.txt') as f:
        buffer = f.read().strip()
    for i in range(4, len(buffer) + 1):
        if len(set(buffer[i-4:i])) == 4:
            start_locations.append(i)
            break
    for j in range(14, len(buffer) + 1):
        if len(set(buffer[j-14:j])) == 14:
            start_locations.append(j)
            break
    return start_locations


if __name__ == '__main__':
    result = day_6()
    print('Start of packet:', result[0])
    print('Start of message:', result[1])
