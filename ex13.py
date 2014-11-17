#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Write a program that asks the user how many Fibonacci numbers to
generate and then generates them. Take this opportunity to think about
how you can use functions. Make sure to ask the user to enter the
number of numbers in the sequence to generate. (Hint: The Fibonacci
sequence is a sequence of numbers where the next number in the sequence
is the sum of the previous two numbers in the sequence. The sequence
looks like this: 1, 1, 2, 3, 5, 8, 13, ...)
'''

def main():
	n = int(float(input("How many in your Fibonacci sequence? ")))
	print (fibonacci(n))
	
def fibonacci(n):
	if n <= 0: return []
	elif n == 1: return [1]
	else:
		fib = [1, 1]
		for x in range(2, n):
			fib.append(fib[x-2] + fib[x-1])
			print (fib)
		return fib
	
if __name__ == "__main__":
	main()