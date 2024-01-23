# check a year either a leap or not.
# taken input from user
# if a year is end at century mean (00) then divide 400.
# if not a century year then divide by 4 and remainder of 0.
year = int(input("Enter a year: "))
if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year.")
elif year % 4 == 0 and year % 100 != 0:
    print(f"{year} is also a leap year.")
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print(f"{year} is not a leap year.")