# #Write your code below this line 👇
#
# def paint_calc(height, width, cover):
#     number_of_cans = (height * width) /cover
#     return number_of_cans
#
# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.
#
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# calc = paint_calc(height=test_h, width=test_w, cover=coverage)
# print(round(calc))
#
# # Prime number checker
# def prime(number):
#     if number==1:
#         print("It is not a prime number")
#     else:
#         is_prime = True
#         for i in range(2,number):
#             if number%i ==0:
#                 is_prime = False
#
#         if is_prime:
#             print("It is a prime number")
#         else:
#             print("It is not a prime number")
#
#
#
#
# prime_number_checker = int(input("Input the number you want to check if it is a prime number"))
#
# prime(number=prime_number_checker)

from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

end_of_program = False
while end_of_program == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    shift = shift%26
    caesar(start_text=text, shift_amount = shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n ")
    if result == 'no':
        end_of_program =True
        print("Goodbye")

