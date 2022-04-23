from random import randint
numFlip = input(" Type 'quit' to exit \nEnter number of flips: ")
while numFlip != 'quit':
    total_heads = 0
    total_tails = 0
    if int(numFlip) > 0:
        for i in range(int(numFlip)):
            flip = randint(0, 1)
            if flip == 0:
                total_heads += 1
            elif flip == 1:
                total_tails += 1
        print(
            f"number of heads: {total_heads}, number of tails: {total_tails}")
        numFlip = input(" Type 'quit' to exit \nEnter number of flips: ")
print("\nThank you for tossing!")
