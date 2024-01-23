# print the prime numbers in an interval
lower = int(input("Enter starting range: "))
upper = int(input("Enter ending range: "))
print(f"print the prime numbers between {lower} and {upper} are: ")
for num in range(lower, upper+1):
    if  num > 1:
        for i in range(2, num):
            if num % i == 0:
               break
        else:
            print(num, end=' ')