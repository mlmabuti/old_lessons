userIn = input("Enter space seperated values: ")
binary = userIn.split()
result = 0

for i in range(len(binary)):
    popped = binary.pop(0)
    result += int(popped, 2)
    if len(binary) == 0:
        break
    else:
        result *= 2
    print(result)
