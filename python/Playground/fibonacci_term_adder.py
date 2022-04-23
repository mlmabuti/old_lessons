def fib_add_terms(nterms):

    i, nth, n1, n2 = 0, 0, 0, 1

    while i < int(nterms):

        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1
        total = nth + n1 - 1

    return total


def fib(nterms):

    if nterms:
        lead, chase = 0, 1

        try:

            for i in range(nterms):
                mover = lead + chase
                chase = lead
                lead = mover

            return lead

    raise Exception('invalid input')


print(fib(0))
print(fib_add_terms(5))
