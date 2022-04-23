from pyautogui import sleep, click, position, typewrite, press, dragTo
import random


def position_check():
    print('Press Ctrl-C to quit.')
    while True:
        x, y = position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


def mouse_click():  # THIS DEPENDS ON YOUR SCREEN AND WINDOW SIZE
    # SO USE POSITION CHECK FIRST
    sleep(2)
    dragTo(1270, 240)
    sleep(2)
    dragTo(1271, 242)
    sleep(2)
    click()

    dragTo(1221, 323)
    sleep(2)
    dragTo(1220, 325)
    sleep(2)
    dragTo(1221, 323)
    sleep(2)
    click()


def wa():
    r = random.randint(1, 3)
    for i in range(1, 3):
        typewrite('$wa')
        press('enter')
        sleep(3)
        if i == r:
            mouse_click()
            typewrite('going dark')
            press('enter')
            return


def main():
    wa()


if __name__ == '__main__':
    sleep(5)
    print("running")
    main()
