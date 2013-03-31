def isPallindrome(num):
	compStr = str(num)
	return compStr == compStr[::-1]

def p4():
	bigPal = -1
	for i in range (999, 100, -1):
		for j in range (i, 100, -1):
			if isPallindrome(i*j):
				bigPal = max(bigPal, i*j)
	return bigPal

print(p4())