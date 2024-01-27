# how to find power of 2 using lambda function
# nums = [1, 2, 3, 4]
# apply a lambda function on nums list
result = list(map(lambda n : 2**n, range(10)))
for i in range(10):
    print("2 raised to power", i, 'is', result[i])