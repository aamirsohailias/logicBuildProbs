# how can we determine the fibonacci sequence??
# define a function with fibo_iter name
def fibo_iter(nterms):
    n1, n2 = 0, 1   # assign and initialize two terms
    count = 2
    """its means runs nterms-2 times -> 
    also remember it loop itereates from 2 to nterms-1"""

    while count < nterms:   # using while loop to generate the fiboSequence
         print(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
        #  print(nth)
         count += 1
if __name__ == '__main__':
    nterms = int(input("how many terms? "))
    fibo_iter(nterms)