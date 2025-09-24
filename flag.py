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
print(flag1)