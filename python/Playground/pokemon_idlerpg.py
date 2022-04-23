import time
from threading import Thread
import pyautogui

# ctrl+c on terminal to stop the program.


def idle_rpg():
    def adventure():
        pyautogui.typewrite("$adventure 2")  # just change adventure
        pyautogui.press("enter")

    def status():
        pyautogui.typewrite("$status")
        pyautogui.press("enter")

    time.sleep(5)
    x = 1
    while (x):
        adventure()
        status()
        time.sleep(3610)  # 1hour = 3600seconds, added 10 for delay
        status()
        print("adventure completed")


def pokemon():
    def route():
        pyautogui.typewrite(".route 6")  # change route number
        pyautogui.press('enter')
        time.sleep(5)  # delay

    def _1():
        pyautogui.typrewrite("1")
        pyautogui.press('enter')

    def _2():
        pyautogui.typewrite("2")
        pyautogui.press('enter')

    def _3():
        pyautogui.typewrite("3")
        pyautogui.press('enter')

    def _4():
        pyautogui.typewrite("4")
        pyautogui.press('enter')

    time.sleep(10)
    x = 1
    while (x):
        route()  # route
        for i in range(0, 2):  # number of times you attack
            _1()
            time.sleep(4)  # delay


if __name__ == '__main__':
    print("running")
    Thread(target=idle_rpg).start()
    Thread(target=pokemon).start()
