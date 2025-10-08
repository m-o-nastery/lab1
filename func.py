CSI = '\x1B['
RESET = f'{CSI}0m'


def graph(width, num):
    if num >= 10:
        if num % 2 == 0:
            print(
                f'{num} |{CSI}47m{" " * width}{CSI}42m{" "}{CSI}47m{" " * (10 + 10 - width)}{RESET}'
            )
        else:
            print(
                f' {num} |{CSI}47m{" " * width}{CSI}42m{" "}{CSI}47m{" " * (10 + 10 - width)}{RESET}'
            )
    else:
        if num % 2 == 0:
            print(
                f' {num} |{CSI}47m{" " * width}{CSI}42m{" "}{CSI}47m{" " * (10 + 10 - width)}{RESET}'
            )
        else:
            print(
                f' {num} |{CSI}47m{" " * width}{CSI}42m{" "}{CSI}47m{" " * (10 + 10 - width)}{RESET}'
            )


def paint(width, num):
    for i in range(1, 12):
        graph(width, num)
        width -= 1
        num -= 1
    print('    0 1 2 3 4 5')


width = 10
num = 10

if __name__ == '__main__':
    paint(width, num)
