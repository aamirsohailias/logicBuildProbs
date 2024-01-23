# check num positive or negative num
def check_num(num):
    if num > 0:
        print(num, "is positive num.")
    elif num == 0:
        print(num, "is equal to zero.")
    else:
        print(num, "is negative num.")
if __name__ == '__main__':
    num = int(input("Enter a integer: "))
    check_num(num)