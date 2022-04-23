terms = input('how many terms? ')
while terms:
    c = 0
    nth = 0
    n1 = 0
    n2 = 1
    while c < int(terms):
        nth = n1 + n2
        n1 = n2
        n2 = nth
        c += 1
        print(n1)
    terms = input('how many terms? ')
