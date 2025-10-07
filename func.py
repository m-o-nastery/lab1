csi = '\x1B['
reset = f'{csi}0m'

def graph(height, width, line, num):
    if num>=10:
        if num%2==0:
            print(f'''{num} |{csi}47m{" "*width}{csi}42m{" "}{csi}47m{" "*(10+10-width)}{reset}''')
        else:
            print(f''' {num} |{csi}47m{" "*width}{csi}42m{" "}{csi}47m{" "*(10+10-width)}{reset}''')
    else:
        if num%2==0:
            print(f''' {num} |{csi}47m{" "*width}{csi}42m{" "}{csi}47m{" "*(10+10-width)}{reset}''')
        else:
            print(f''' {num} |{csi}47m{" "*width}{csi}42m{" "}{csi}47m{" "*(10+10-width)}{reset}''')
width = 10
line = 1
num = 10
for height in range(1,12):
    graph(height,width,line,num)
    width -= 1
    num -= 1
print(f'    0 1 2 3 4 5')