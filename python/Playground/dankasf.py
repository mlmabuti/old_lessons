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


def memey():
    if low_priority:
        arr = ['blacktwitter', 'chucknorris', 'comics',
               'discordmeme', 'joke', 'meirl', 'prequel', 'pun', 'sequel']
        write('pls ' + choice(arr))
        press('enter')
        sleep(randint(5, 8))


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


def high_low():
    arr = ['high', 'low', 'jackpot']
    write('pls hl')
    press('enter')
    sleep(randint(2, 5))
    write(choice(arr))
    press('enter')
    sleep(randint(2, 5))


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


def random_word():
    arr = ["meh", "shit", "ok", "alright", "dope",
           "dank", "hmmm", "ehh", "damn", "okay", "nice", "gg",
           "ggwp"]
    write(choice(arr))
    press('enter')
    sleep(randint(2, 6))


def low_priority():
    f = randint(0, 40)
    if f == 3:
        return True
    return False


def main():
    arr = [guess, random_word, bal, postmemes, trivia, beg, dig,
           fish, hunt, level, random_word, high_low]

    while 1:
        shuffle(arr)
        for f in arr:
            f()
        if stop_chance():
            write('brb')
            press('enter')
            sleep(180)
        sleep(randint(20, 40))


if __name__ == '__main__':
    sleep(5)
    print('...running')
    main()
