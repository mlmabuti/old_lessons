def alt_reverse():

    number = 9
    alt = 1

    while number**3 >= alt:
        print(number, alt, end=' ')
        alt += 1
        number -= 1


alt_reverse()


def celsius_farenheit():

    x = " "
    while x:
        print("\nMain Menu\na. Celsius to Fareneheit\nb. Farenheit to Celsius\nc. Exit")
        x = input('\nChoose option [a,b, or c]:').lower()

        if x == 'a':
            print("Celsius - Farenheit Conversion")
            c = float(input("Enter Celsius: "))
            f = 9 / 5 * c + 32
            print("Farenheit equivalent is", round(f, 2))

        elif x == 'b':
            print("Farenheit - Celsius Conversion")
            f = float(input("Enter Farenheit: "))
            c = (f - 32) * 5 / 9
            print("Celsius equivalent is", round(c, 2))

        elif x == 'c':
            print("Goodbye")
            x = ''

        else:
            raise("Invalid Input")


def SumOfOddNumber():
    i, odd, c = 1, 0, 0
    #terms = int(input("Enter number of terms: "))
    terms = 6
    while c < terms:

        print(i)
        odd += i
        c += 1
        i += 2
    print('sum of odds', odd)


def number_of_dimes():

    num = 7250

    thousands = num // 1000
    print(thousands)

    hundreds = num - (thousands * 1000) // 100
    print(hundreds)


celsius_farenheit()
