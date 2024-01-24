# how can we determine armstrong number
# define a function
def check_armstrong_num(num):
    sum = 0
    # Changed num variable to string, 
    # and calculated the length (number of digits)
    order = len(str(num))
    # find the sum of the cube of each digit
    temp = num
    for i in range(1, order+1):  # also use a while loop (temp > 0) or temp != 0.
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    # display the result
    if num == sum:
       print(num, 'is armstrong num.')
    else:
       print(num, 'is not armstrong number.')
if __name__ == '__main__':
    num = int(input('Enter an integer: ')) # taken input from user
    check_armstrong_num(num)   # call a function