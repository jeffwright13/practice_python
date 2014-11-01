#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

def get_divisors(n):
	divs = []
	count = 1
	while count <= n:
		if n % count == 0:
			divs.append(count)
		count += 1
	return divs

def main():
	integer = input("Please input a positive integer: ")
	num = abs(int(float(integer)))
	divisors = get_divisors(num)
	for elem in divisors:
		print(elem)
		
if __name__ == "__main__":
	main()