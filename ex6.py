#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Ask the user for a string and print out whether this string is a
palindrome or not. (A palindrome is a string that reads the same
forwards and backwards.)
'''

def main():
	str = input ("Please enter a string to check for palindromicity: ")
	is_it = (str.strip()).lower()
	print (is_palindrome(is_it))

def is_palindrome(list):
	list_rev = list[::-1]
	return (list_rev == list)
		
if __name__ == "__main__":
	main()