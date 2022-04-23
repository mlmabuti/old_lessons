# Coding Challenge 1
# Problem 1
def problem1():
    string = "Something other than Hello, World!"
    print(string)
    # Problem 2


def problem2():
    l = ['pizza', 'apple', 'cauliflower']
    for i in l:
        print(i)
        # Problem 3


def problem3():
    age = int(input('enter age: '))
    if age <= 10:
        print('age is less than or equal to 10')
    elif age > 10 and age < 26:
        print('11 to 25')
    else:
        print('26+')
        # Problem 4


def problem4():
    a = None
    inp_1 = int(input("Enter dividend: "))
    inp_2 = int(input("Enter divisor: "))
    a = inp_1 / inp_2
    print(a)
