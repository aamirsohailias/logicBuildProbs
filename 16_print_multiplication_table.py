# how we print the multiplication table
# taken input from user
num = int(input("Display multiplication table of? "))
counter = 1
while counter <= 10:
    product = num * counter
    # counter += 1
    print(num, '*', counter, '=', product)
    counter += 1