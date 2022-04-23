#from threading import Thread
from pyautogui import sleep, press, typewrite as write
from random import choice, randint, shuffle


def stop_chance():
    if randint(1, 20) == 3:
        print("1 in 20 just occured.")
        return True
    return False


def guess():
    write('pls guess')
    press('enter')
    for i in range(0, 4):
        write(str(randint(1, 20)))
        sleep(randint(1, 3))
        press('enter')
    sleep(randint(3, 6))


def bal():
    write('pls bal')
    press('enter')
    sleep(randint(2, 4))
    if randint(0, 4) == 2:
        dep()


def dep():
    write('pls dep all')
    press('enter')
    sleep(randint(2, 6))


def postmemes():
    arr = ['f', 'r', 'i', 'c', 'k']
    write('pls postmemes')
    press('enter')
    sleep(randint(2, 4))

    write(choice(arr))
    press('enter')
    sleep(randint(3, 6))


def trivia():
    arr = ['a', 'b', 'c', 'd']
    write('pls trivia')
    press('enter')
    sleep(randint(2, 4))

    write(choice(arr))
    press('enter')
    sleep(randint(3, 6))


def beg():
    write('pls beg')
    press('enter')
    sleep(randint(3, 6))


def dig():
    write('pls dig')
    press('enter')
    sleep(randint(2, 6))


def fish():
    write('pls fish')
    press('enter')
    sleep(randint(2, 6))


def hunt():
    write('pls hunt')
    press('enter')
    sleep(randint(2, 6))


def level():
    write('pls level')
    press('enter')
    sleep(randint(2, 4))


def active():
    write('pls level --active')
    press('enter')
    sleep(randint(2, 6))


def lottery():
    write('pls with all')
    press('enter')
    sleep(3)
    write('pls lottery')
    press('enter')
    sleep(2)
    write('yes')
    press('enter')


def buy_laptop():
    write('pls with all')
    press('enter')
    sleep(3)
    write('pls buy laptop 5')
    press('enter')
    sleep(3)
    write('yes')
    press('enter')


def random_word():
    arr = ["meh", "shit", "ok", "alright", "dope",
           "dank", "hmmm", "ehh", "damn", "okay", "nice", "gg",
           "ggwp"]
    write(choice(arr))
    press('enter')
    sleep(randint(2, 6))


def main():
    arr = [guess, bal, postmemes, trivia, beg, dig,
           fish, hunt, level, random_word]

    while 1:
        for i in range(0, 3):
            for i in range(0, 268):
                shuffle(arr)
                for f in arr:
                    f()
                if stop_chance():
                    write('brb')
                    press('enter')
                    sleep(randint(120, 180))
                else:
                    sleep(randint(20, 40))
            lottery()
        sleep(randint(1800, 3600))


if __name__ == '__main__':
    sleep(5)
    print('...running')
    main()
