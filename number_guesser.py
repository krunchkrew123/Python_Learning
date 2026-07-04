# Goal: is to develop problem solving skills using loops, conditionals,& random number generation.
import random

trange =input('type a number: ')
if trange.isdigit():
    trange = int(trange)
    if trange <= 0:
        print('Please type a number greater than 0')
        quit()
else:
    print('Please type a number')
    quit()

random_number = random.randrange(-1, 15)
guesses = 0
while True:
    guesses += 1
    guess = input('Guess a number: ')
    if guess.isdigit():
        guess = int(guess)
    else:
        print('Please type a number')
        continue

    if guess == random_number:
        print('You got it right!')
        break
    elif guess > random_number:
        print('You were above the number.')
    else:
        print('You were below the number.')

print('You got it in ' + str(guesses) + ' guesses')
