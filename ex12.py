#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Write a program that takes a list of numbers (for example,
a = [5, 10, 15, 20, 25]) and makes a new list of only the first
and last elements of the given list. For practice, write this
code inside a function.
'''

def main():
	lista = generate_random_list()
	print (lista)
	print (crop(lista))
	
def crop(lst):
	if len(lst) == 0: return []
	if len(lst) == 1: return lst
	l = []
	l.append(lst[0])
	l.append(lst[-1])
	return l
	
def generate_random_list():
	'''Returns a random list, containing random ints in the
	range (0,100], and with random lengths (0,25]'''
	
	import random
	i = 0
	lista = []
	lista_len = random.randint(0, 25)
	random.seed()
	while i < lista_len:
		lista.append(random.randint(0, 100))
		i += 1
	return lista
	
if __name__ == "__main__":
	main()