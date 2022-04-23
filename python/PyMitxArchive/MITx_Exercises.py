# =============================================================================
# # EXERCISE 1 : LOOPS
# =============================================================================

def q1():
    num = 5
    if num > 2:
        print(num)
        num -= 1
    print(num)


def q2():
    num = 0
    while num <= 5:
        print(num)
        num += 1
    print("Outside of loop")
    print(num)


def q3():
    num = 10
    while num > 3:
        num -= 1
        print(num)


def q4():
    num = 10
    while True:
        if num < 7:
            print('Breaking out of loop')
            break
        print(num)
        num -= 1
    print('Outside of loop')
# =============================================================================
# # EXERCISE 2 : LOOPS
# =============================================================================


def q5():
    n = 0
    while n < 10:
        n += 2
        print(n)
    print("Goodbye!")


def q6():
    for i in range(2, 11, 2):
        print(i)
    print("Goodbye!")


def q7():
    end = 'abcdefghijklmnopqrstuvwxyz'
    range_end = end + 1
    total = 0
    for i in range(range_end):
        total += i
    print(total)
# =============================================================================
# # EXERCISE 3 : LOOPS
# =============================================================================


def q8():
    num = 5
    if num > 2:
        print(num)
        num -= 1
    print(num)


def q9():
    num = 10
    for num in range(5):
        print(num)
    print(num)


def q10():
    divisor = 2
    for num in range(0, 10, 2):
        print(num/divisor)


def q11():
    for variable in range(20):
        if variable % 4 == 0:
            print(variable)
        if variable % 16 == 0:
            print('Foo!')


def q12():
    count = 0
    for letter in 'Snow!':
        print('Letter # ' + str(count) + ' is ' + str(letter))
        count += 1
        break
    print(count)
# =============================================================================
# # EXERCISE 4 : LOOPS
# =============================================================================


def q13():
    myStr = '6.00x'
    for char in myStr:
        print(char)
    print('done')


def q14():
    greeting = 'Hello!'
    count = 0
    for letter in greeting:
        count += 1
        if count % 2 == 0:
            print(letter)
        print(letter)
    print('done')


def q15():
    school = 'Massachusetts Institute of Technology'
    numVowels = 0
    numCons = 0
    for char in school:
        if char == 'a' or char == 'e' or char == 'i' \
           or char == 'o' or char == 'u':
            numVowels += 1
        elif char == 'o' or char == 'M':
            print(char)
        else:
            numCons -= 1
    print('numVowels is: ' + str(numVowels))
    print('numCons is: ' + str(numCons))
# =============================================================================
# #EXERCISE 5 : LOOPS
# =============================================================================


def q16():
    iteration = 0
    count = 0
    while iteration < 5:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1


def q17():
    count = 0
    phrase = "hello, world"
    for iteration in range(5):
        index = 0
        while index < len(phrase):
            count += 1
            index += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))


def q18():
    count = 0
    phrase = "hello, world"
    for iteration in range(5):
        count += len(phrase)
        print("Iteration " + str(iteration) + "; count is: " + str(count))
# =============================================================================
# # EXERCISE 6 : LOOPS
# =============================================================================


def q22():
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
            if iteration % 2 == 0:
                break
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1


def q23():
    iteration = 0
    count = 0
    while iteration < 5:
        # the variable 'letter' in the loop stands for every
        # character, including spaces and commas!
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1


def q24():
    iteration = 0
    while iteration < 5:
        count = 0
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))
        iteration += 1
