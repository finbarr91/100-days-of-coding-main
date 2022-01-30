# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)
# print(fruit)

# Code to calculate student's average height

# # 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split(", ")
# sum_student_heights = 0
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆
#   sum_student_heights = sum_student_heights + student_heights[n]
#   count = n+1
# print(count)
# print(sum_student_heights)
# print(round(sum_student_heights/count))

# student_heights = input("Type in the students' heights").split()
# for n in range(len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
# print(type(student_heights[n]))
#
# sum_of_heights = 0
# for height in student_heights:
#     sum_of_heights = sum_of_heights+height
#
# print(sum_of_heights)
#
# count = 0
# for count in range(len(student_heights)):
#     count = count+1
# print(count)
#
# print(round(sum_of_heights/count))


# Student score
# student_scores = input("Input a list of student scores").split(" ")
# for i in range(len(student_scores)):
#     student_scores[i] = int(student_scores[i])
# print(student_scores)
#
# scores =0
# for score in student_scores:
#     if score>scores:
#         scores = score
# print(f"The highest score is {scores}")

# Add numbers from 0 to 2000

# sum =0
# for number in range(1, 5001):
#     sum= sum+number
# print(sum)

# sum=0
# for even_number in range(2,101,2):
#     sum = sum+even_number
# print(sum)
#
# sum =0
# for even_number in range(1,101):
#     if even_number%2==0:
#         sum=sum+even_number
# print(sum)

# FizzBuzz challenge

# for number in range(1,5001):
#     if number%3 ==0 and number%5==0:
#         print("FizzBuzz")
#
#     elif number%3 ==0:
#         print("Fizz")
#     elif number%5 ==0:
#         print("Buzz")
#     else:
#         print(number)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

char_of_password = []
for nr_letter in range(nr_letters):
    index_of_letters = random.randint(0, len(letters) - 1)
    letter = letters[index_of_letters]
    char_of_password+=letter

print(char_of_password)


for nr_symbol in range(nr_symbols):
    index_of_symbols = random.randint(0,len(symbols)-1)
    symbol = symbols[index_of_symbols]
    char_of_password+=symbol
print(char_of_password)


for nr_number in range(nr_numbers):
    index_of_numbers = random.randint(0,len(numbers)-1)
    number = numbers[index_of_numbers]
    char_of_password+=number
print(char_of_password)
    # print(f"{random.shuffle([number])}")

# password = letter_of_password+symbol_of_password+number_of_password
# print(type(password))
# print(password)

shuffle_password = random.sample(char_of_password,len(char_of_password))
print(shuffle_password)

shuffle_password1=char_of_password.copy()
shuffle_password2 = random.shuffle(char_of_password)
print(shuffle_password2)

shuffle_password = "".join(shuffle_password)
print(shuffle_password)

str_password = ""
for element in shuffle_password:
    str_password = str_password+element

print(f"Your password is {str_password}")
