import random
num = int(random.randrange(1, 50))
count = 0
while True:
    awnser = int(input('Type a number between 1 and 50: '))
    if awnser == num: 
        print(f'\nCongratulations! The right number was {num}!\nYou guessed the number with {count} attempts!')
        print('='*45)
        break
    elif awnser < num:
        print(f'\nThe number {awnser} is below the chosen one!')
        count += 1
        print('-'*45)
    elif awnser > num:
        print(f'\nThe number {awnser} is above the chosen one!')
        count += 1
        print('-'*45)
    else:
        print('\nType a valid value!')
        print('-'*45)