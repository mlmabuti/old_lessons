import random


def main():
    p = ''
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&?'
    for i in range(25):
        p += characters[random.randint(0, len(characters)-1)]
    print(p)


if __name__ == '__main__':
    print('running...')
    for i in range(int(input('enter number of passwords to generate: '))):
        main()
