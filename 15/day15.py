import re


def day15(y: int):
    with open('day15_input.txt') as f:
        positions = set([])
        sensors = set([])
        beacons = set([])
        while True:
            report = f.readline().strip()
            if not report:
                break
            report = report.split(': ', maxsplit=1)

            sensor = [int(i) for i in re.sub(r'[^\d\s-]', '', report[0]).strip().split()]
            beacon = [int(i) for i in re.sub(r'[^\d\s-]', '', report[1]).strip().split()]
            if sensor[1] == y:
                sensors.add(sensor[0])
            if beacon[1] == y:
                beacons.add(beacon[0])

            distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

            r = distance - abs(sensor[1] - y)
            if r > 0:
                x_pos = sensor[0]
                for i in range(r + 1):
                    positions.add(x_pos + i)
                    positions.add(x_pos - i)

    positions.difference_update(sensors)
    positions.difference_update(beacons)

    return len(positions)


if __name__ == '__main__':
    print('Positions without beacon:', day15(2000000))
