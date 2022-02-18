from random import choice

MAX_TRIES = 8
GAME_NAME = 'hangman'
PLAY_GAME = 'play'
EXIT_GAME = 'exit'

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript']
    program_choice = list(choice(words))
    word_len = len(program_choice)
    mask = list(word_len * '-')
    tries = MAX_TRIES
    stock_letters = []

    while tries:
        print(f'\n{"".join(mask)}')
        if not '-' in mask:
            print('You guessed the word!\nYou survived!\n')
            break
        else:
            user_input = input('Input a letter: ')
            if len(user_input) != 1:
                print('You should input a single letter')
                continue
            elif not user_input.islower():
                print('Please enter a lowercase English letter')
                continue
            if not user_input in program_choice and not user_input in stock_letters:
                print("That letter doesn't appear in the word")
                tries -= 1
            elif user_input in mask or user_input in stock_letters:
                print("You've already guessed this letter")
            else:
                for i in range(word_len):
                    if user_input == program_choice[i]:
                        mask[i] = user_input
            stock_letters.append(user_input)
    if not tries:
        print("You lost!\n")

print(' '.join(GAME_NAME.upper()))

while True:
    game_state = input(f'Type "{PLAY_GAME}" to play the game, "{EXIT_GAME}" to quit: ')
    if game_state == PLAY_GAME:
        hangman()
    elif game_state == EXIT_GAME:
        break