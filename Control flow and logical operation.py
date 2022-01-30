# number = int(input("Which number do you want to check?\n"))
#
# if number%2==0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

#
# height = float(input('Enter your height in m:\n'))
# weight = float(input('Enter your weight in kg:\n'))
#
# BMI = round(weight/height**2)
#
#
# if BMI <18.5:
#     print(f"Your BMI is {BMI} therefore your are underweight ")
# elif BMI<25:
#     print(f"Your BMI is {BMI} therefore your are normal weight ")
# elif BMI <30:
#     print(f"Your BMI is {BMI} therefore your are overweight ")
# elif BMI <35:
#     print(f"Your BMI is {BMI} therefore your are obese ")
# else:
#     print(f"Your BMI is {BMI} therefore your are clinically obese ")

# # Leap year challenge:
# year = int(input("Which year do you want to check?"))
#
# if year%4==0:
#     if year%100 !=0 or year%400 ==0:
#         print("leap year")
#     else:
#         print("Not a leap year")
# else:
#     print("Not a leap year")
#
# # Write your code here:
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 ==0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not leap year")

# Rollercoaster challenge
#
# height = int(input("What is your height"))
# bill = 0
#
# if height >120 :
#     print("Can ride")
#     age = int(input("What is your age"))
#     if age<12:
#         bill = 5
#     elif age <18:
#         bill = 7
#     else:
#         bill =12
#
#     want_photo = input("Do you want a photo Type Y or N")
#     if want_photo == "Yes".lower() or want_photo == "Y".lower():
#         bill+=3
#     print(f"Your total bill is {bill}")
# else:
#     print("Can't ride")

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S,M, or L")
# add_pepperoni = input("Do you want pepperoni? Y or N")
# extra_cheese = input("Do you want extra cheese? Y or N")

# if size == "S".lower():
#     price = 15
#     if add_pepperoni == "Y".lower():
#         price =price+2
#     if extra_cheese =="Y".lower():
#         price = price+1
#     print(f"total price is ${price}")
# elif size == "M".lower:
#     price = 20
#     if add_pepperoni == "Y".lower():
#         price = price + 3
#     if extra_cheese == "Y".lower():
#         price = price + 1
#     print(f"total price is ${price}")
# else:
#     price = 25
#     if add_pepperoni == "Y".lower():
#         price = price + 3
#     if extra_cheese == "Y".lower():
#         price = price + 1
#     print(f"total price is ${price}")

# bill = 0
#
# if size == 'S'.lower():
#     bill+=15
# elif size =="M".lower():
#     bill+=20
# elif size == "L".lower():
#     bill +=25
#
# if add_pepperoni =="Y".lower():
#     if size =="S".lower():
#         bill +=2
#     else:
#         bill+=3
#
# if extra_cheese =="Y".lower():
#     bill +=1
#
# print(f"you total bill is {bill}")

# # True Love calculator
# print("Welcome to the Love Calculator")
# name1 = input("What is your name?\n").lower()
# name2 = input("What is their name?\n").lower()
# bothnames = name1+" "+name2
# print(bothnames)
#
#
# t = bothnames.count("t")
# r = bothnames.count("r")
# u = bothnames.count("u")
# e = bothnames.count("e")
#
# true = str(t+r+u+e)
#
# l = bothnames.count("l")
# o = bothnames.count("o")
# v = bothnames.count("v")
# e = bothnames.count("e")
#
# love = str(l+o+v+e)
#
# true_love_score = true+love
# true_love_score = int(true_love_score)
#
# if (true_love_score<10 )or (true_love_score>90):
#     print(f"Your score is {true_love_score}, you go together like coke and mentos ")
#
# elif true_love_score>=40 and true_love_score<=50:
#     print(f"Your score is {true_love_score}, you are alright")
#
# else:
#     print(f"Your score is {true_love_score}")

# print("Welcome to Treasure Island.\n"
#       "Your Mission is to find the Treasure!")
# left_right = input("Type left or right").lower()
# if left_right== 'left':
#     swim_wait = input("Do you want to swim or wait").lower()
#     if swim_wait == 'wait':
#         which_door = input("Choose one of the door, red, blue,Yellow").lower()
#         if which_door == "yellow":
#             print("You win")
#         else:
#             print("Game over")
#
#     else:
#         print('Game over')
# else:
#     print("game over")

