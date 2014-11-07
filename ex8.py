#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
import sys

def main():
	num_s = input('How many rounds would you like to play? ')
	num = int(float(num_s))
	
	i = 0
	while i < num:
		i += 1
		
	print('Thanks for playing!')
	again = input('Would you like to play again? ')
	if "y" in again.strip().lower():
		main()
	else:
		sys.exit()

if __name__ == "__main__":
	main()