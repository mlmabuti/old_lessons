def sqrt(number):
    i = 0
    while i**2 < abs(number):
        i += 1
    if i**2 % number != 0:
        raise Exception('%g is not a perfect square' % number)
    else:
        print(i)


sqrt(80)


def cbrt(number):
    i = 0
    while i**3 < abs(number):
        i += 1
    if i**3 % number != 0:
        raise Exception('%g is not a perfect cube.' % number)
    else:
        print(i)


cbrt(81)
