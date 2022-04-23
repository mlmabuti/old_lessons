def cube_guesser():
    x = int(input("Enter integer: "))
    i = 0
    while i**3 < abs(x):
        i += 1
        print(i)
    if i**3 != abs(x):
        print(f"{x} is not a perfect cube")
    else:
        print(f'the cube root of {x} is {i}')


def square_guesser():
    x = int(input("Enter integer: "))
    i = 0
    while i**2 < abs(x):
        i += 1
        print(i)
    if i**2 != abs(x):
        print(f"{x} is not a perfect cube")
    else:
        print(f'the cube root of {x} is {i}')


inp = input('type "quit" to exit\ncalculate square or cube? ').lower()
if inp == 'square':
    while x != 'quit':
        square_guesser()
elif inp == 'cube':
    while x != 'quit':
        cube_guesser()
else:
    print('invalid entry')
