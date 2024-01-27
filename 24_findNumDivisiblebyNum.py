# how to find numbers divisible by another number
my_list = [12, 65, 54, 39, 102, 339, 221,]

result = list(filter(lambda n : n%13 == 0, my_list))

# Check the length of the filtered list
print("Length of result:",len(result))

# Iterate over the filtered list
for i in range(len(result)):
     print(i, 'is', (result[i]))