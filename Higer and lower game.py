from game_data import data
from art_high_and_low import logo
import random
from art_high_and_low import vs

print(logo)

def A_choice():
    choice_A = random.randint(0, 49)
    choice_A = data[choice_A]
    choice_A_follower_count = choice_A["follower_count"]
    print(choice_A)
    print(f"Compare A: {choice_A['name']} a {choice_A['description']} from {choice_A['country']}")
    return choice_A_follower_count

def B_choice():
    choice_B = random.randint(0, 49)
    choice_B = data[choice_B]
    choice_B_follower_count = choice_B["follower_count"]
    print(choice_B)
    print(f"Compare B: {choice_B['name']} a {choice_B['description']} from {choice_B['country']}")
    return choice_B_follower_count

def game():
    current_score =0
    end_game = False
    while end_game ==False:
        choice_A_follower_count= A_choice()
        print(vs)
        choice_B_follower_count=B_choice()

        if choice_A == choice_B:
            choice_B = random.choice(data)
        # Comparison of the two choices
        computer_choice = ""
        if choice_B_follower_count>choice_A_follower_count:
            choice_B_follower_count =str(choice_B_follower_count)
            choice_B_follower_count = "B"
            computer_choice+=choice_B_follower_count

        elif choice_A_follower_count>choice_B_follower_count:
            choice_A_follower_count =str(choice_A_follower_count)
            choice_A_follower_count ="A"
            computer_choice += choice_A_follower_count
        print(computer_choice)

        user_choice = input("Who has more followers, Type 'A' or 'B' \n")
        if user_choice.lower() == computer_choice.lower():
            current_score +=1
            print(f"You are right! Current score is {current_score}")
        elif user_choice.lower() != computer_choice.lower():
            current_score = current_score
            print(f"You are wrong! Current score is {current_score}")
            end_game =True

game()


