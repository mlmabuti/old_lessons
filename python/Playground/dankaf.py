import time
from pyautogui import typewrite, sleep, press
from random import choice, randint, shuffle


def guess():
    typewrite('pls guess')
    sleep(2)
    press('enter')
    for i in range(0, 4):
        typewrite(str(randint(1, 20)))
        sleep(2)
        press('enter')
    sleep(3)


def memey():
    random_sleep = randint(7, 12)
    arr = ['4chan', 'blacktwitter', 'chucknorris', 'comics',
           'discordmeme', 'joke', 'meirl', 'prequel', 'pun', 'sequel']
    typewrite('pls ' + choice(arr))
    sleep(2)
    press('enter')
    sleep(random_sleep)


def bal():
    sleep(2)
    typewrite('pls bal')
    press('enter')
    random_sleep = randint(2, 6)
    sleep(random_sleep)
    r = randint(0, 4)
    if r == 2:
        dep()


def shop():
    random_sleep = randint(2, 6)
    number = str(randint(2, 5))
    typewrite('pls shop ' + number)
    press('enter')
    sleep(random_sleep)


def inv():
    random_sleep = randint(2, 6)
    number = str(randint(2, 4))
    typewrite('pls inv ' + number)
    press('enter')
    sleep(random_sleep)


def dep():
    random_sleep = randint(2, 6)
    typewrite('pls dep all')
    press('enter')
    sleep(random_sleep)


def postmemes():
    random_sleep = randint(2, 6)
    arr = ['f', 'r', 'i', 'c', 'k']
    typewrite('pls postmemes')
    press('enter')
    sleep(random_sleep)

    random_sleep = randint(1, 3)
    typewrite(choice(arr))
    press('enter')
    sleep(random_sleep)


def trivia():
    random_sleep = randint(2, 6)
    arr = ['a', 'b', 'c', 'd']
    typewrite('pls trivia')
    press('enter')
    sleep(random_sleep)

    random_sleep = randint(2, 4)
    typewrite(choice(arr))
    press('enter')
    sleep(random_sleep)


def beg():
    random_sleep = randint(2, 6)
    typewrite('pls beg')
    press('enter')
    sleep(random_sleep)


def dig():
    random_sleep = randint(2, 6)
    typewrite('pls dig')
    press('enter')
    sleep(random_sleep)


def fish():
    random_sleep = randint(2, 6)
    typewrite('pls fish')
    press('enter')
    sleep(random_sleep)


def hunt():
    random_sleep = randint(2, 6)
    typewrite('pls hunt')
    press('enter')
    sleep(random_sleep)


def level():
    r = randint(0, 1)
    if r:
        random_sleep = randint(2, 6)
        typewrite('pls level')
        press('enter')
        sleep(random_sleep)


def active():
    r = randint(0, 5)
    if not r:
        random_sleep = randint(2, 6)
        typewrite('pls level --active')
        press('enter')
        sleep(random_sleep)


def random_word():
    random_word = ["bark", "mighty", "yourself", "finally", "rays", "what"
                   "climate", "any", "cabin", "sure", "laugh", "paid"
                   "city", "excitement", "different", "buy", "article", "way"
                   "dinner", "soil", "hearing", "stop", "hearing", "broad"
                   "population", "hand", "off", "exclaimed", "giving", "young"
                   "riding", "buried", "poet", "including", "early", "do"
                   "surface", "graph", "skin", "use", "dot", "wheel"]
    typewrite(choice(random_word))
    press('enter')


def chance():
    flip = randint(0, 20)
    if flip == 3:
        print("5% just happened")
        return True
    return False


arr_functions = [guess, random_word, postmemes,
                 bal, trivia, level, beg, dig, fish, hunt]


def main():
    x = 1
    while x:
        random_sleep = randint(20, 35)
        shuffle(arr_functions)
        for f in arr_functions:
            f()
        sleep(random_sleep)
        r = randint(0, 1)
        if r:
            active()
        if chance():
            sleep(150)


if __name__ == '__main__':
    print("running")
    sleep(120)
    main()
