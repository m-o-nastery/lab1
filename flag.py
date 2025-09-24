csi = '\x1B['
reset = f'{csi}0m'
flag1 = f'''
{csi}41m{' '*50}{reset}
{csi}41m{' '*50}{reset}
{csi}47m{' '*50}{reset}
{csi}47m{' '*50}{reset}
{csi}44m{' '*50}{reset}
{csi}44m{' '*50}{reset}
'''
def flag2(color):
    print(f'{csi}{color}m{' '*50}{reset}')
    print(f'{csi}{color}m{' '*50}{reset}')
colors = [41,47,44]
for color in colors:
    flag2(color)
print(flag1)