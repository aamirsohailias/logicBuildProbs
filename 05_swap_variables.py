# how to swap two variables
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
"""
if variables value are only {numeric or integer} then we would use followed method.
"""
num_1 = num_1 + num_2
num_2 = num_1 - num_2
num_1 = num_1 - num_2

# temp = num_1
# num_1 = num_2
# num_2 = temp

print("after swapping value of (num_1) {0} and (num_2) {1}.".format(num_1, num_2))