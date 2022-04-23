insample = input("Enter space seperated value sample: ")
listsample = insample.split()

sumsample = 0
for i in listsample:
    sumsample += int(i)
mean = sumsample / len(listsample)

sumsample_square = 0
for i in listsample:
    sumsample_square += (int(i) - mean)**2

variance = sumsample_square / (len(listsample) - 1)
standard_deviation = variance**(1/2)

print("mean = ", round(mean, 2))
print("variance = ", round(variance, 2))
print("standard deviation = ", round(standard_deviation, 2))
