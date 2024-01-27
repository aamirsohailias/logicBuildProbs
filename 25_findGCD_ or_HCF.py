# find the hcf or gcd using euclidean Algorithm
# define a function
def find_hcf(n1, n2):
    minimum_num = min(n1, n2)
    maximum_num = max(n1, n2)
    # using a while loop, 
    # The loop will persist (jaari rhy ga) until the variable "mini" becomes zero.
    while minimum_num:
        # make a temp var and store mini var value in it because when loop will end 
        # mini var must have been zero.
        temp = minimum_num
        minimum_num = maximum_num % minimum_num
        maximum_num = temp
    return maximum_num
if __name__ == '__main__':
    # taken input from user
    var1st = int(input("Enter val 1st: "))
    var2nd = int(input("Enter val 2nd: "))
    # find the gcd
    gcd = find_hcf(var1st, var2nd)
    print(f"hcf of {var1st} and {var2nd} is {gcd}.") # print the output of gcd
