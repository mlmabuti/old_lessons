def loop():
    selection = input("\n\nChoose from 1 to 9\n1.) binary to hexa\n2.) binary to octal\n3.) binary to decimal\n4.) octal to hexa\n5.) octal to binary\n6.) octal to decimal\n7.) hexa to binary\n8.) hexa to octal\n9.) hexa to decimal\nSelection: ")

    if selection == '1':
        binaryToHexa()
    elif selection == '2':
        binaryToOctal()
    elif selection == '3':
        binaryToDecimal()
    elif selection == '4':
        octalToHexa()
    elif selection == '5':
        octalToBinary()
    elif selection == '6':
        octalToDecimal()
    elif selection == '7':
        hexaToBinary()
    elif selection == '8':
        hexaToOctal()
    elif selection == '9':
        hexaToDecimal()
    else:
        print("invalid entry")


def re():
    p = input("again? enter y/n: ")
    if p == "y":
        loop()
    elif p == "n":
        print("byebye")

# binary to hexa


def binaryToHexa():
    binary = int(input("Enter binary number: "), 2)
    print("in hexadecimal " + hex(binary))
    re()
# binary to octal


def binaryToOctal():
    binary = int(input("Enter binary number: "), 2)
    print("in octal " + oct(binary))
    re()
# binary to decimal


def binaryToDecimal():
    binary = int(input("Enter binary number: "), 2)
    print("in decimal " + binary)
    re()

# octal to hexa


def octalToHexa():
    octal = int(input("Enter octal number: "), 8)
    print("in hexadecimal " + hex(octal))
    re()
# octal to binary


def octalToBinary():
    octal = int(input("Enter octal number: "), 8)
    print("in binary" + bin(octal))
    re()
# octal to decimal


def octalToDecimal():
    octal = int(input("Enter octal number: "), 8)
    print("in decimal " + octal)
    re()

# hexa to binary


def hexaToBinary():
    hexa = int(input("Enter hexadecimal number: "), 16)
    print("in binary " + bin(hexa))
    re()
# hexa to octal


def hexaToOctal():
    hexa = int(input("Enter hexadecimal number: "), 16)
    print("in octal " + oct(hexa))
    re()
# hexa to decimal


def hexaToDecimal():
    hexa = int(input("Enter hexadecimal number: "), 16)
    print("in decimal "+hexa)
    re()


loop()
