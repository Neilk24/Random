import random

options=['Rock', 'Paper', 'Scissors']

user_choice=input('Choose your weapon. Paper, Rock, or Scissors: ')
computer_choice=random.choice(options)

if user_choice==computer_choice:
    print('The game is a tie. Please try again to try and win!')
elif user_choice=='Rock' and computer_choice=='Scissors':
    print('Rock smashes Scissors. You win!')
elif user_choice=='Paper' and computer_choice=='Rock':
    print('Paper covers up Rock. You win!')
elif user_choice=='Scissors' and computer_choice=='Paper':
    print('Scissors cuts Paper. You win!')
else:
    print('You lose! Imagine losing to a computer, cannot be me. Please try again.')