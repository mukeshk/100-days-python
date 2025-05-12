def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

#In Plain English
#If a year is divisible by 4 → it might be a leap year.
#If it’s also divisible by 100 → it is not a leap year,
#Unless it is divisible by 400 → then it is a leap year

print(is_leap_year(2024))
