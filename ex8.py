#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
import sys

def play_game():
	# get input from players
	p1_s = input('Player 1: Rock, paper or scissors (r/p/s)? ')
	p1 = p1_s.strip().lower()[0]
	p2_s = input('Player 2: Rock, paper or scissors (r/p/s)? ')
	p2 = p2_s.strip().lower()[0]
	
	if p1 == p2: return 'tie'
	elif p1 == 'r':
		if p2 == 'p': return 'P2'
		else: return 'P1'
	elif p1 == 'p':
	    if p2 == 'r': return 'P1'
	    else: return 'P2'
	elif p1 == 's':
		if p2 == 'r': return 'P2'
		else: return 'P1'
		
def show_stats():
	pass

def update_stats(w):
	pass

def main():
	# get input from players
	num_s = input('How many rounds would you like to play? ')
	num = int(float(num_s))
	if num <0: sys.exit()
	
	# main execution loop
	i = 0
	while i < num:
		winner = play_game()
		update_stats(winner)
		i += 1
		
	# game over; see if player wants to play again
	print('Thanks for playing!')
	show_stats()
	again = input('Would you like to play more? ')
	if "y" in again.strip().lower():
		main()
	else:
		sys.exit()

if __name__ == "__main__":
	main()