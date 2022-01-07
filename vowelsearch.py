def search4vowels(word:str)->set:
	"""Display any vowels found in a supplied-for word."""
	vowels = set('aeiou')
	#word = input('Provide a word to search for vowels: ')
	#found = vowels.intersection(set(word))
	#for vowel in found:
	#	print(vowel)
	return vowels.intersection(set(word))

print(search4vowels(input("Enter a word: ")))
help(search4vowels)