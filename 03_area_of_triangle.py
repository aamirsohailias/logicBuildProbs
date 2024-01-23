# calculate the area of trianlge with heron's formula
# define a function with 3 arguments
def area_of_triangle(a, b, c):
    # We need to figure out the semi-perimeter first.
    s = (a+b+c)/2
    # calculate the area of triangle
    area = (s*(s-a)*(s-b)*(s-c)) **0.5
    return area
if __name__ == '__main__':
    # taken 3 sides of triangle from user
    side_1 = int(input("Enter 1st side: "))
    side_2 = int(input("Enter 2nd side: "))
    side_3 = int(input("Enter 3rd side: "))
    calculate_area = area_of_triangle(side_1, side_2, side_3)
    # output area of triangle
    print("The area of triangle is {0:.2f}.".format(calculate_area))
