

def transform(arr):
	return [sum(arr)*j for j in arr]


def reverse(string):
	return string[::-1]


if __name__=='__main__':
	print(reverse("to be reversed"))
	print(transform([1,2,3,4,5,6]))