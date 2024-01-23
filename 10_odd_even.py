# python program to check if the input num is odd or even.
# a number is even if division by 2 gives a remainder of 0.
# taken input from user
num = int(input("Enter a integer: "))
if num % 2 != 0 :
    print(f"{num} is odd.")
else:
    print(f"{num} is even.")