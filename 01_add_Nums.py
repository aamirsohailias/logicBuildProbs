# how to add two numbers using python
# define a function with two perameters adding numbers
def add_fun():
    sum = 0
    while True:
        num = int(input("enter integer: "))
        if num < 0:break
        sum += num
        # num += 1
    return sum
if __name__ == '__main__':
    # num_1 = int(input("Enter an 1st_integer: "))
    # num_2 = int(input("Enter an 2nd_integer: "))
    # sumOfNum = add_fun(num_1, num_2)
    print("sum of numbers: ", add_fun())
