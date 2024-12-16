import random
playing=True
number=str(random.randint(10, 20))

print('I will have a number between 10 and 20 in my mind. You have to guess it.')
print('Keep guessing until you get the correct number.')

while playing:
    guess=input('Guess a number: ')
    
    if guess==number:
        print('Good job, you guessed the number!')
        print('The number was:',number)
        break
    else:
        print('Wrong number. Please guess again.')