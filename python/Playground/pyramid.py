rows = 30
for i in range(rows):
    print()
    for space in range(rows-i-1):
        print('.', end='')
    for star in range(2*i+1):
        print('*', end='')
