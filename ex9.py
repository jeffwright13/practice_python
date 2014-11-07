#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

import sys, random

def main():
	num_guesses = 0
	while 1:
		guess_str = input('Please guess an integer between 1 and 9 (inclusive), or type "exit" to quit: ')
		if guess_str.strip().lower() == 'exit':
			print('You guessed {} tiimes.'.format(num_guesses))
			sys.exit()
		num_guesses += 1
		guess = int(float(guess_str))
		answer = random.randint(1, 9)
		if guess == answer:
			print('Nice work! You got it right!')
		elif guess < answer:
			print ('Too low. Sorry.')
		else:
			print('Too high. Sorry.')

if __name__ == "__main__":
	main()