def iterative_comparison(left: list, right: list) -> str:
    for i in range(max(len(left), len(right))):
        try:
            l = left[i]
        except IndexError:
            return 'True'
        try:
            r = right[i]
        except IndexError:
            return 'False'
        if type(l) == int:
            if type(r) == int:
                if l < r:
                    return 'True'
                elif l > r:
                    return 'False'
            elif type(r) == list:
                l = [l]
        if type(l) == list:
            if type(r) == int:
                r = [r]
            if type(r) == list:
                result = iterative_comparison(l, r)
                if result:
                    return result


def day13():
    index = 0
    indices = 0
    packets = []

    with open('day13_input.txt') as f:
        while True:
            index += 1
            try:
                left = eval(f.readline().strip())
            except SyntaxError:
                break
            right = eval(f.readline().strip())
            f.readline()
            if left == '':
                break

            if eval(iterative_comparison(left, right)):
                indices += index
            packets.extend([left, right])

        packet_1 = 1
        packet_2 = 2
        for packet in packets:
            if eval(iterative_comparison(packet, [[2]])):
                packet_1 += 1
            if eval(iterative_comparison(packet, [[6]])):
                packet_2 += 1

    return indices, packet_1 * packet_2


if __name__ == '__main__':
    index_sum, index_product = day13()
    print('Index sum:', index_sum)
    print('Index product:', index_product)
