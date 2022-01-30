import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#Step 1

word_list = ["aardvark", "baboon", "camel"]

chosen_word_index = random.randint(0,len(word_list)-1)
chosen_word = word_list[chosen_word_index]

lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')
# Showing the display
display = []
for letter in range(len(chosen_word)):
    display+="_"
print(display)

#TODO-1: - Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display'
# has no more blanks ("_"). Then you can tell the user they've won.

finished_guess = False

while finished_guess == False:
    # guess of the word
    guess = input("Guess a letter").lower()

    for index,character in enumerate((chosen_word)):
      if guess in character:
          display[index] = guess

    if guess not in chosen_word:
        lives-=1
        if lives ==0:
            finished_guess =True
            print("You lose")

    print(f"{''.join(display)}")

    if "_" not in display:
        finished_guess =True
        print("You win")

    print(stages[lives])
