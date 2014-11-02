#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''

def main():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	print (common(a, b))
	
def common(a, b):
	'''
	Returns a list that contains all common elements in two lists
	passed into the function.
	'''
	c = []
	for elem in a:
		if elem in b:
			if elem not in c:
				c.append(elem)
	return c
		
if __name__ == "__main__":
	main()