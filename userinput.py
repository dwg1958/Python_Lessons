print("USER INPUT")
print('')

import random
maxn = 10
n = random.randint(1, maxn)
tries = 0

print('Welcome to guess the number game!')
print('Guess the number from 1 to %d' % maxn)
guess = None
while guess != n:
    guess = int(input('Your try: '))
    if guess > n:
        print('Nope - Too high')
    if guess < n:
        print('Sorry - Too low')
    tries += 1

print(f'Congratulations, the answer was {n} - you won in {tries} attempts!')
