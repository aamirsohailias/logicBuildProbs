# print the armstrong number in interval
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print(f"print the armstrong numbers between {lower} and {upper} are: ")
for num in range(lower, upper+1):
    temp = num
    sum = 0
    order = len(str(num))
    while temp > 0:
        digit = temp % 10
        sum += digit**order
        temp //= 10
    if sum == num:
        print(num)    