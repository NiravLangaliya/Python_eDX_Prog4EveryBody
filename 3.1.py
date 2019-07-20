"""
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly.
"""

hrs = input("Enter Hours:")
h = float(hrs)

rateperhours = input("Enter Rate per Hours")
rh=float(rateperhours)

if h > float(40):
	gross_pay = ((h-40)*rh*1.5)+(float(40)*rh)
else:
    gross_pay = h*rh

print(gross_pay)