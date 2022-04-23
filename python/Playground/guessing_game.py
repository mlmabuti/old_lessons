from random import randint
guess = input("enter a random number from 1 to 10: ")
a = True
while a == True:
    ans = randint(1, 10)
    while guess != ans:
        if guess == 'quit':
            print('thanks for playing!')
            a = False
            break
        elif int(guess) > ans:
            print("Lower!")
            guess = input("enter a random number from 1 to 10: ")
        elif int(guess) < ans:
            print("Higher!")
            guess = input("enter a random number from 1 to 10: ")
        else:
            print("You are correct: ", guess)
            guess = input("enter a random number from 1 to 10: ")
            break
