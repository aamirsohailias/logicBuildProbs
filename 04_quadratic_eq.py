# how to solve quadratic equation ??? ax^2 + bx + c = 0
# we need to import cmath module 1st then
# define a function with perimeters to solve problem in easy way.
import cmath
def solve_quadratic_eq(a, b, c):
    # we hove to find discriminant 1st
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    # find the two solutions
    root1 = (-b + discriminant) / 2*a
    root2 = (-b - discriminant) / 2*a
    return root1, root2
if __name__ == '__main__':
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    c = int(input("Enter 3rd value: "))
    equation = solve_quadratic_eq(a, b, c)
    print("The solutions of quadratic eq are {0}.".format(equation))
