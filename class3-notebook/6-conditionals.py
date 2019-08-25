import random

random_number = random.randint(0,100)

if random_number == 100:
    print('You won the great prize')
elif random_number >= 50:
    print('You won a small prize')
elif random_number > 25:
    print('You didn\'t get anything! But play again for free!')
else:
    print('You won nothing')
