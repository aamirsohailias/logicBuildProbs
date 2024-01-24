sum = 0
while True:
    num = int(input("Enter integer: "))
    if num < 0: break
    sum += (num)
    # num+=1
print(sum)


print("----------------------")
num = int(input("Enter number: "))
sum = 0
while num > 0:
    sum += num
    num -= 1
print(sum)