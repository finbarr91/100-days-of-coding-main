# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages:"))
# word_per_page == int(input("Number of words per page:"))
# total_words= pages * word_per_page
# print(total_words)

# Use a dubugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])

for number in range(1,101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number%3 ==0:
        print("Fizz")
    elif number%5 ==0:
        print("Buzz")
    else:
        print(number)