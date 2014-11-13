#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to [Exercise 4] to help you. Take this opportunity to practice using functions, described below.
'''

def main():
	num = int(float(input('Please enter an integer: ')))
	print (is_prime(num))

def get_divisors(n):
	divs = []
	count = 1
	while count < n:
		if n % count == 0:
			divs.append(count)
		count += 1
	return divs
	
def is_prime(n):
	divs = get_divisors(n)
	if divs == [] or divs == [1]:
		return True
	else:
		return False
	
if __name__ == "__main__":
	main()