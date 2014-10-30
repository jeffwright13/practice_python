#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Ex 1:

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

(1) Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)

(2) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

from datetime import date

def main():
	name = get_name()
	age = get_age()
	bday_yet = birthday_yet()
	year = get_year(int(age), bday_yet)
	
	if year == 'greater':
		print ("You're already 100 years old or greater! Congrats!")
	else:
		print ('Hello, {}!'.format(name))
		print ('You will turn 100 in the year {}.'.format(year))

def get_name():
	return (input('Please enter your name:'))

def get_age():
	return (input('Please enter your age:'))
	
def birthday_yet():
	ans = input('Have you had your birthday yet this year (y/n)?')
	if 'y' in ans.lower():
		return True
	else:
		return False

def get_year(a, b):
	assert a >= 0, "Age is not allowed to be less than zero."
	if a >= 100:
		return 'greater'
	else:
		today = str(date.today()).split('-')
		if bool(b) == True:
			this_year = int(today[0])
			return (this_year + (100 - a))
		else:
			this_year = int(today[0])
			return (this_year + (99 - a))
		
if __name__ == "__main__":
	main()