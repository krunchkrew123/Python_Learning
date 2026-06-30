# Goal: Practice user input, conditional logic, and basic program flow in python
print('Welcome to my quiz!')

playing = input('Do you want to play? ')
if playing != 'yes':
    print('Thanks for playing')
    quit()
print('Okay, Lets play')
#Create first question
question1 = input('What is the capital of france? ')
if question1.lower() == 'paris':
    print('Correct!')
else:
    print('Incorrect! Paris, was the correct answer.')
# repeat for questions 2-5
question2 = input('What is the capital of germany? ')
if question2.lower() == 'berlin':
    print('Correct!')
else:
    print('Incorrect! Berlin, was the correct answer.')

question3 = input('What is the capital of spain? ')
if question3.lower() == 'madrid':
    print('Correct!')
else:
    print('Incorrect! Madrid, was the correct answer.')

question4 = input('What is the capital of italy? ')
if question4.lower() == 'rome':
    print('Correct!')
else:
    print('Incorrect! Rome, was the correct answer.')

question5 = input('What is the capital of russia? ')
if question5.lower() == 'moscow':
    print('Correct!')
else:
    print('Incorrect! Moscow, was the correct answer.')
