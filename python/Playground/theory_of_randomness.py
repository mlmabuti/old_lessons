# just had a thought. if the odds of an event is 1/30 and you do it 8 times and in those 8 times you randomly pick 1
# then let's test 1/30*8*1/8 is still 1/30 by running like thousands of simulations

import random
import statistics


def for_a(n):
    a = 0

    for x in range(n):
        rng = random.randint(0, 29)

        i = random.randint(0, 29)
        if i == rng:
            a += 1

    return a


def for_b(n):
    b = 0

    for x in range(n):
        rng = random.randint(0, 29)
        r = []
        for i in range(0, 8):
            r.append(random.randint(0, 29))
        if r[random.randint(0, len(r)-1)] == rng:
            b += 1

    return b


def for_c(n):
    c = 0

    for x in range(n):
        rng = random.randint(0, 29)
        r = []
        for y in range(8, 0, -1):
            for i in range(0, y):
                r.append(random.randint(0, 29))
        if r[random.randint(0, len(r)-1)] == rng:
            c += 1

    return c


def main():
    a = []
    b = []
    c = []

    for i in range(10000):
        a.append(for_a(30))
        b.append(for_b(30))
        c.append(for_c(30))

    avg_a = statistics.mean(a)
    avg_b = statistics.mean(b)
    avg_c = statistics.mean(c)

    print("a", avg_a)
    print("b", avg_b)
    print("c", avg_c)

    #a = 0
    #b = 0

    # for i in range(20):
    #    if for_a(30000) > for_b(30000):
    #        a += 1
    #    else:
    #        b += 1
    #print(a," ", b)


if __name__ == "__main__":
    main()
