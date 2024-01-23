# how to convert the kilometers to miles
# define a function
def find_miles(km):
    # conversion factor
    mile_1 = 1.60934
    miles = km / 1.60934
    return miles
if __name__ == '__main__':
    k_meter = float(input("Enter the kilometers: "))
    how_much_miles = find_miles(k_meter)
    print("how much miles which we cover the distance %0.3f miles."%(how_much_miles))

print('-------------------------------')

miles = float(input("Enter value in miles: "))
# conversion factor
conv_fact = 0.621371
# calculate kilometers
kilo_meters = miles / 0.621371
print("%0.2f miles is equal to %0.2f kilometers"% (miles, kilo_meters))