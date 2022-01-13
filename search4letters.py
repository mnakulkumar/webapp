def search4letters(phrase:str, letters:str='aeiou') -> set:
	"""Return a set of the 'letters' found in 'phrase'."""
	return set(letters), intersection(set(phrase))

print(search4letters(input("Input a string"),input("input a string")))