import math
# x = [1,2,3,4,5]
# print(len(x))

# x = input("Type in your input")
# y,z= x
# print(int(y)+int(z))
# y=6/4
# y = math.floor(y)
# print(y)
#
# height = float(input('Enter your height in m:\n'))
# weight = float(input('Enter your weight in kg:\n'))
#
# BMI = round(weight/height**2)
# print(f"Your BMI is {BMI}")
#
# age = int(input("What is your current age?\n"))
# maximum_age = 90
# age_left = 90 - age
# days_left = age_left*365
# weeks_left = age_left*52
# months_left = age_left*12
#
# print(f"You have {days_left} days,{weeks_left} weeks, and {months_left} months left")

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill\n"))
percentage_tip = float(input("What percentage tip would you like to give? 10, 12 or 15\n"))
number_of_people = int(input("How many people to split the bill?\n"))

percentage_tip_calc = percentage_tip/100*total_bill
total_bill_calc = total_bill+percentage_tip_calc
bill_for_each_person = round(total_bill_calc/number_of_people,2)
print(f"Each person should pay: ${bill_for_each_person}")

