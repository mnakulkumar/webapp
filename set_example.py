vowels2 = { 'a', 'e', 'e', 'i', 'o', 'u', 'u'}


vowels = set('aeiou')
word = 'hello'

u = vowels.union(set(word))
u_list = sorted(list(u))
u_list

d = vowels.difference(set(word))

