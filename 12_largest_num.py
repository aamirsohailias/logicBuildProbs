# how to find the largest number among three numbers
# define a function 
def find_largest_num(x, y, z):
    if x >= y and x >= z:
        largest = x
        # print("{0} is a largest number.".format(x))
    elif y >= x and y >= z:
        largest = y
        # print("{0} is a largest number.".format(y))
    else:
        largest = z
        # print("{0} is a largest number.".format(z))
    return largest
if __name__ == '__main__':
    print("largest number is:", find_largest_num(2, 12, 11))

