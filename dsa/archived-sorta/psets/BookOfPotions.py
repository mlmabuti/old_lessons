#Harry wants to find Voldemort's potion making book but he is confused about how to get it.
#
#The book has a special ISBN(International Standard Book Number) which is  unique numeric book identifier only for Voldemort's book printed on it. The ISBN is based upon a 10-digit code. The ISBN is valid if:
#1xdigit1 + 2xdigit2 + 3xdigit3 + 4xdigit4 + 5xdigit5 + 6xdigit6 + 7xdigit7 + 8xdigit8 + 9xdigit9 + 10xdigit10 is divisible by 11.
#Help Harry to find the book! 

arr = input()

def isbn_checker(arr):
    i = 1
    product_total = 0
    arr = [int(x) for x in arr]
    for x in arr:
        product_total += x*i
        i += 1

    if product_total % 11 == 0:
        return print("Legal ISBN")

    return print("Illegal ISBN")

isbn_checker(arr)