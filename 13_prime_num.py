# check prime number is a prime number or not
# taken input from user
num = int(input("Enter an integer: "))
if num <= 1:
    print(f"{num} is not a prime number.")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if num % i == 0:
            print(f"{num} is not a prime number.")
            print(i, 'times', num // i, 'is', num)
            break
    else:
        print(f"{num} is a prime number.")
