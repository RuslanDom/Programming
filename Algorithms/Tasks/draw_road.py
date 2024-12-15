row = 20
column = 50
# left_bord = 18
# right_bord = 30
for r in range(row):
    for c in range(column):
        if r == 9:
            print('-', end='')
        elif c == 24:
            print('|', end='')
        elif c == -r + 18:
            print('/', end='')
        elif c == r + 30:
            print('\\', end='')
        else:
            print(' ', end='')
    # left_bord -= 1
    # right_bord += 1
    print()