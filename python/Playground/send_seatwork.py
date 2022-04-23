from pyautogui import position, sleep, click, moveTo, press, hotkey


def positionCheck():
    #572, 734
    while True:
        x, y = position()
        positionStr = 'X: ' + str(x).rjust(4) + 'Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


def main():
    sleep(60*18)
    print('starting')
    moveTo(570, 734)
    click()
    hotkey('ctrl', 'v')
    press('enter')
    print('done')


if __name__ == '__main__':
    main()
