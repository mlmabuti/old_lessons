n = input("Enter n: ")

for i in range(1,int(n)+1):
    if i % 5 == 0 and i % 3 == 0:
        print("fizzBuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)