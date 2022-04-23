string = "ihffninsanoiefnjoiasejfniojesoffnifniijnsiodfjasdfasdf"
count = 0
for i in range(len(string)):
    if string[i:i+3] == 'fni':
        count += 1
print(count)
