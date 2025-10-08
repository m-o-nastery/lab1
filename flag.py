csi = '\x1B['
reset = f'{csi}0m'


def flag2(color):
    print(f'{csi}{color}m{" " * 50}{reset}')
    print(f'{csi}{color}m{" " * 50}{reset}')


colors = [41, 47, 44]


def flag():
    for color in colors:
        flag2(color)


if __name__ == '__main__':
    flag()
