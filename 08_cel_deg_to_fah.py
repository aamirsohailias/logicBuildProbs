# how to convert temperatue celsius degree to fahrenheit
# taken input from user in celsius_degree
celsius_degree = float(input("Enter degree in celsius: "))
# calculate fahrenheit
fahrenheit_degree = (celsius_degree * 1.8) + 32
print("{0:0.2f} celsius degree is equal to {1:0.2f} fahrenheit degree.".format(celsius_degree, fahrenheit_degree))

print("---------------------------------------------")

# convert temperature fahrenheit degree to celsius degree
# temperature in fahrenheit degree
fahren_degree = float(input("Enter in fahrenheit degree: "))
# conversion degree
celsius_degree = (fahren_degree-32) / 1.8
print("%0.1f degree fahren is equal to %0.1f degree celsius."%(fahren_degree, celsius_degree))
