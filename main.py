import random

no_of_guesses = 0
no_of_attempt = 10
print('Hello! I am thinking of a number between 1 and 20.You have {} no. of attempt.'.format(no_of_attempt))

number = random.randint(1, 20)

while no_of_guesses < no_of_attempt:
    print('Take a guess.')
    guess_num = int(input())
    no_of_guesses = no_of_guesses + 1
    if guess_num < number:
        print('Your guess is too low.')
    if guess_num > number:
        print('Your guess is too high.')
    if guess_num == number:
        print('Nice,You guessed my number in {} guesses!'.format(no_of_guesses))
        break
if guess_num != number:
    print('Nope. The number I was thinking {}'.format(number))