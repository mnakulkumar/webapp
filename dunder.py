print('We start off in:', __name__)
if __name__ == '__main__':
	print('And end up in:', __name__)

def myFunction():
	print("Within myFunction , current namespace is", __name__)

myFunction()