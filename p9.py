natural_squares = []

def find_squares(limit):
	i = 1
	sq = i*i
	limit_sq = limit * limit
	while sq <= limit_sq:
		natural_squares.append(sq)
		i += 1
		sq = i*i

def pythag_triple(limit):

	for a in range(1, limit/3):
		for b in range(a, (limit-1)/2):
			for c in range(b, limit):
				py_sum = a + b + c
				if py_sum == 1000 and a < b < c:
					a2 = a*a
					b2 = b*b
					c2 = c*c
					if a2 + b2 == c2:
						return [a, b, c]
	return []

def p9(c):
	find_squares(c)
	triple = pythag_triple(c)
	if len(triple) == 0:
		return "Failure"
	print(triple)
	product = 1
	for num in triple:
		product *= num
	return product

print(p9(1000))
