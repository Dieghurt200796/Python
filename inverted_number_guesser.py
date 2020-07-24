import time, random

''' 
1. Contains a model of its environment.
2. Can act in its environment.
3. Can update its model of its environment.
'''

print('''

Welcome to the inverted number guesser.
Pick a number between 1 and 100.''')

time.sleep(5)

min_max = [[1, 100]]

guess = None

correct = False

guesses = 0

def make_guess():

    current_min, current_max = min_max[len(min_max) - 1]

    guess = random.randint(current_min, current_max)
    print('My guess is ' , guess, '.', sep='')
    
    return guess

def get_feedback():


    feedback = input('Is that \'Too low\', \'Too high\', or \'Correct\'?\n')
    if feedback.lower() == "too low":
        print("Okay.")
        return 1
    elif feedback.lower() == "too high":
        print("Okay.")
        return -1
    elif feedback.lower() == "correct":
        print("Nice.")
        return 0
    else:
        print("Invalid input.")
        return None

#make_guess()

def update_model(guess, feedback):
    current_min, current_max = min_max[len(min_max) - 1]
    new_boundary = guess + feedback
    print(new_boundary)
    if new_boundary == current_min or new_boundary == current_max:
        print('That feedback makes no sense.')
        return

    # Replace the minimum
    if feedback == 1:
        min_max.append([new_boundary, current_max])

    # Replace the maximum
    elif feedback == -1:
        min_max.append([current_min,new_boundary])
    
    if min_max[-1][0] > min_max[-1][1]:
        print('ERROR: Boundaries overlap.')
        # Delete the last added min and max
        min_max.pop()
    

while not correct:
    print(f"Current boundaries {min_max[-1]}")
    guess = make_guess()
    feedback = get_feedback()
    update_model(guess, feedback)
    guesses += 1

    if feedback == 0:
        correct = True

print(f"It took {guesses} guesses.\nThanks for playing.")
