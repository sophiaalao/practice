

def fibonnaci():
	a, b = 1, 1
	count = 0

	while count < 100:
		yield a 
		a, b = b,  a + b
		count += 1


g = fibonnaci()

for  num in g:
	print(num)