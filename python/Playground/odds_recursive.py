def odd(num1, num2):
    if num1 > num2:
        return
    print(num1, end=" ")
    return odd(num1+2, num2)
