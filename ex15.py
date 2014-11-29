#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in reverse order. For example, say I type the string "My name is Michele", then the result would be "Michele is name My".
'''

def main():
	sentence = input('Enter a sentence:')
	print (reverse(sentence))

def reverse(str):
	pass
	
if __name__ == "__main__":
	main()