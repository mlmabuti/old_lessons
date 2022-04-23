insample = input("Enter space seperated value sample: ")
listsample = insample.split()

sumsample = 0
for i in listsample:
    sumsample += int(i)
mean = sumsample / len(listsample)

x_minus_mean = [int(listsample[i])-mean for i in range(len(listsample))]

x_sqr = [x_minus_mean[i]**2 for i in range(len(listsample))]

variance = (sum(x_sqr) / len(listsample))

standard_deviation = variance**(1/2)

print("mean =", round(mean, 2))
print("variance =", round(variance, 2))
print("standard deviation =", round(standard_deviation, 2))

# ====================================================== #
# WITHOUT USING LIST COMPREHENSION                       #
# ====================================================== #

# FOR LOOP MEAN
# sumsample = 0
# for i in len(listsample):
#     sumsample += int(i)
# mean = sumsample / len(listsample)
# print(round(mean,2))

# FOR LOOP xs1 - mean
# v = []
# for i in range(lensample):
#     v.append(round(int(listsample[i]) - mean,3))
#     print(v)

# FOR LOOP VARIANCE
# for i in x_sqr:
#     numerator += i
# variance = round(numerator / lensample, 3)
# print(variance)

# NO NEED TO LOOP STANDARD DEVIATION, JUST SQRT THE VARIANCE
# ======================================================= #
