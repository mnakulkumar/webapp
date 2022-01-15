def search4vowels(word:str) -> set:
	"""Display any vowels found in a supplied-for word."""
	vowels = set('aeiou')
	return vowels.intersection(set(word))
	
#print(search4vowels(input("Enter a word: ")))

def search4letters(phrase:str, letters:str='aeiou') -> set:
	"""Return a set of the 'letters' found in 'phrase'."""
	return set(letters).intersection(set(phrase))

#print(search4letters(input("Input a string"),input("input a string")))
