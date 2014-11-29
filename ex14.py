#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3

'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:
- Write two different functions to do this - one using a loop and constructing a list, and another using sets.
- Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

def main():
	list1 = [-1, 0, -1, 2, 2, 90, 85, -1, 66, 0.6, 66]
	list2 = generate_random_list
	print (remove_dupes_1(list1))

def remove_dupes_1(lst):
	return list(set(lst))
	
def remove_dupes_2(lst):
	pass

def remove_dupes_3(lst):
	dupes = []
	for elem in lst:
		pass
	return lst - dupes
	
def generate_random_list():
	'''Returns a random list, containing random ints in the
	range (0,100], and with random lengths (0,25]'''
	
	import random
	i = 0
	list = []
	list_len = random.randint(0, 25)
	random.seed()
	while i < lista_len:
		list.append(random.randint(0, 100))
		i += 1
	return list
	
if __name__ == "__main__":
	main()