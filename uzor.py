csi = '\x1B['
reset = f'{csi}0m'

def x(offset,gap,paint,offset2):
    print(f'{csi}47m{" "*offset}{csi}40m{" "*paint}{csi}47m{" "*gap}{csi}40m{" "*paint}{csi}47m{" "*offset2}{csi}40m{" "*paint}{csi}47m{" "*gap}{csi}40m{" "*paint}{csi}47m{" "*offset}{reset}')
offset = 9
gap = 16
paint = 5
offset2 = 0
f = True
for i in range(9):
    if gap == 0:
        f = False
    x(offset,gap,paint,offset2)
    x(offset,gap,paint,offset2)
    if f == False:
        offset-=2
        gap+=4
        offset2-=4
    else:
        offset+=2
        gap-=4
        offset2+=4