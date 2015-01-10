#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra: Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import random
import string

def main():
	length = input('Enter length:')
	password = generate_password(length)
	print (password)
	
def generate_password(length):
	letters = string.letters
	digits = string.digits
	chars = letters + digits
	password = ''

	for k in range(0, length):
		password += str(random.choice(chars))
	
	return password
	
if __name__ == "__main__":
	main()