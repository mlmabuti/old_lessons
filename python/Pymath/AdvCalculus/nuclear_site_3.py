# x = true
p = 60_000
i = 1
a = p*2
while True:
    p *= 1.05
    if p >= a:
        print(i)
        break
    i += 1
