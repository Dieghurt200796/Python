# Create a Python program that will think of random integer between 1 and 100,
# and then allow the user to guess the number, giving the feedback of 'Too low' or 'Too high'.

import random

number = random.randint(1, 100)

correct = False

games = 0

guesses = []


def invalid():
    def is_digit(string):
        if not guess.isdigit():
            print('Invalid input, try again (your input must be an integer).')
            return False
        else:
            return True
    
    def is_valid(number):
        if number <= 0 or number >= 101:
            print('Invalid input, try again (youu input must be a valid integer between 1 and 100).')
            return False
        else:
            return True

    guess = input()
    while not is_digit(guess) or not is_valid(int(guess)):
        guess = input()
    
    return int(guess)


def make_guess():

    if len(guesses) == 0:
        print('What is the number?')
        guess = invalid()
        # guesses += [guess]
        guesses.append(guess)
    
    else:
        print('Try again.')
        guess = invalid()
        # guesses += [guess]
        guesses.append(guess)
    
    return guess


def check_guess():
    if guess < number:
        
        print('Too low.', end=' ')
        return -1
    elif guess > number:
        print('Too high.', end=' ')
        return 1
    else:
        print('Correct! You took', len(guesses), 'guesses!')
        # exit()
        return 0


while correct == False:
    guess = make_guess()
    is_correct = check_guess()
    if is_correct == 0:
        correct = True

    while correct == True:
        games += 1
        retry = input('Do you want to try again? (Only answer with Yes/No) ')
        if retry.lower() == 'yes':
            guesses.clear()

            number = random.randint(1, 100)
            correct = False
            # make_guess()
        elif retry.lower() == 'no':
            buffer = ''
            buffer += f'\nThanks for playing, you played {games} game'
            if not games == 1:
                buffer += 's'
            buffer += '.\n'
            print(buffer)
            exit()
        else:
            print('Invalid input.')
    
        



# print(number)