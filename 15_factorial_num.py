# how to find the factorial of number??
# define a function for finding factorial number.
def find_fact(num):
    fact = 1
    if num == 1 or num == 0:
        return 1
    elif num > 1:
        for n in range(2, num+1):
            fact *= n
        return fact
if __name__ == '__main__':
    num = int(input("enter num: "))
    print(f"factorial of {num} is {find_fact(num)}.")