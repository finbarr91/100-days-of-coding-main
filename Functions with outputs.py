# Functions with outputs

# def format_name(f_name,l_name):
#     """Take a first and last name and format it to return the title case version of the name"""
#     formated_f_name=f_name.title()
#     formated_l_name=l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
# result= format_name("angela", "Angela")
# print(result)
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# #
# def format_name(f_name,l_name):
#     if f_name == "" or l_name =="":
#         return " You did not provide a valid input"
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()
#     return f"Result: {formatted_f_name} {formatted_l_name}"
#
# result = format_name(f_name=first_name,l_name=last_name)
# print(result)

# def is_leap(year):
#     """Take a first and last name and format it to return the title case version of the name"""
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
#
# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) == True and month == 2:
#         days = 29
#         return days
#     return month_days[month - 1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)
#
# num1 = int(input("What is the first number?"))
# num2 = int(int("What is the second number"))


for i in range(3):
    print(i)
    for j in range(4):
        print("####")