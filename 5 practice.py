

TARGET = 100
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def add(digit, sign, branches):
	for i in range(len(branches)):
		branches[i] = str(digit) + sign + str(branches[i])

	return branches


def f(summ, number, index):
	digit = abs(number) % 10

	if(index >= len(values)):
		if(summ == number):
			result = []
			result.append(str(digit))
			return result
		else:
			return []

	branch1 = f(summ - number, values[index], index + 1)
	branch2 = f(summ - number, -values[index], index + 1)

	concatenatedNumber =  10 * number + values[index] if number >= 0 else 10 * number - values[index]

	branch3 = f(summ, concatenatedNumber, index + 1)

	results = []

	results.extend(add(digit, "+", branch1))
	results.extend(add(digit, "-", branch2))
	results.extend(add(digit, "",  branch3))

	return results 



r = f(TARGET, values[0], 1)

for result in r:
	print(result)



