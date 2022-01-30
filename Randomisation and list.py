import random
#
# choice = random.randint(0,1)
#
#
# if choice == 1:
#     print("Heads")
# else:
#     print("Tail")

# names_string = input("Give everybody's names, separated by a comma.\n")
# names = names_string.split(", ")
#
# choice = random.choice(names)
# print(f"{choice} will pay for the bill")
#
# choice = random.randint(0,len(names)-1)
# choice = names[choice]
# print(f"{choice} will pay for the bill")

# 🚨 Don't change the code below 👇
# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
#
# map = [row1,row2,row3]
# print(f"{row1}\n,{row2}\n,{row3}\n")
#
# position = input("Where do you want to put the treasure")
# horizontal = int(position[0])
# vertical = int(position[1])
# map[horizontal-1][vertical-1]='X'
#
# print(f"{row1}\n,{row2}\n,{row3}\n")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
game_choice = ["rock", "paper", "scissors"]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player_choice >2 or type(player_choice) == str:
    print("Your choice is Invalid and therefore, you lost")
else:

    player_or_user_choice = game_choice[player_choice]

    print(f"Your choice is {player_choice}")
    #
    computer_choice = random.randint(0,len(game_choice)-1)
    computer_choice= game_choice[computer_choice]
    print(f"Computer choice is {computer_choice}")

    if player_or_user_choice == "rock" and computer_choice == "scissors":
        print("You win")
    elif player_or_user_choice == "scissors" and computer_choice == "paper":
        print("You win")
    elif player_or_user_choice == "paper" and computer_choice == "rock":
        print("You win")
    elif player_or_user_choice == computer_choice:
        print("It is a draw")

    else:
        print("You lost")

# Example
#
# Print i as long as i is less than 6:

# i = 0
# while i<6:
#     print(i)
#     i+=1
#
# # Example
# #
# # Exit the loop when i is 3:
#
# i = 1
# while i < 6:
#     print(i)
#     if i ==3:
#         break
#     i=i+1
#
# i = 1
# while i<6:
#     print(i)
#     i=i+1
# else:
#     print(f"{i} is no longer less than 6")

# for x in "banana":
#     print(x)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     if fruit == 'banana':
#         continue
#     print(fruit)

# for i in range(6):
#     print(i)
# else:
#     print("It is finished")
#
# for i in range(6):
#     if i ==3:
#         break
#     print(i)
# else:
#     print("It is finished")

# adjectives = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for adjective in adjectives:
#     for fruit in fruits:
#         print(adjective,fruit)

for i in [0,1,2]:
    pass