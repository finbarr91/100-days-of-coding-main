import random
print("Welcome to the Number Guessing Game!\nI am thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty level, type easy for 'easy' and hard for 'hard'\n")
chosen_number = random.randint(1,100)
# print(f"The chosen number is {chosen_number}")


def easy():
    finished_game = False
    while finished_game == False:
        if difficulty_level == 'easy'.lower():
            lives = 10
            for life in range(1,11):
                print(f"You have {lives} remaining to guess the number")
                make_a_guess = int(input("Make a guess"))
                if lives != 0:
                    if make_a_guess ==chosen_number:
                        print(f"The Chosen number {chosen_number} matches your guess, therefore Congratulation!")
                        finished_game=True
                        break
                    elif make_a_guess > chosen_number:
                        print("Too high")
                        if lives != 1:
                            print("Guess again")
                    elif make_a_guess < chosen_number:
                        print("Too low")
                        if lives != 1:
                            print("Guess again")

                lives-=1
                if lives ==0 and make_a_guess!= chosen_number:
                    print(f"Game over, You lost\nAnyway the number is {chosen_number}")
                    finished_game =True

def hard():
    finished_game = False
    while finished_game == False:
        lives = 5
        for life in range(1,6):
            print(f"You have {lives} remaining to guess the number")
            make_a_guess = int(input("Make a guess"))
            if lives != 0:
                if make_a_guess ==chosen_number:
                    print(f"The Chosen number {chosen_number} matches your guess, therefore Congratulation!")
                    finished_game=True
                    break
                elif make_a_guess > chosen_number:
                    print("Too high")
                    if lives != 1:
                        print("Guess again")
                elif make_a_guess < chosen_number:
                    print("Too low")
                    if lives != 1:
                        print("Guess again")

            lives-=1
            if lives ==0 and make_a_guess!= chosen_number:
                print(f"Game over, You lost\nAnyway the number is {chosen_number}")
                finished_game =True

if difficulty_level == 'easy'.lower():
    easy()
else:
    hard()

