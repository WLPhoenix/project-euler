primes = []

import math
def findPrimes(limit):
	flags = [True] * limit
	flags[0] = flags[1] = False

	for(i, isprime) in enumerate(flags):
		if isprime:
			primes.append(i)
			for n in xrange(i, limit, i):		
				flags[n] = False
	return primes

def factors(num):
	if num == 1:
		return []
	for i in primes:
		if i > num:
			break
		if num % i == 0:
			recFactors = factors(num/i)
			recFactors.append(i)
			return recFactors
	return [num]


def p5(limit):
	limit += 1
	findPrimes(limit)
	factMaps = []
	for i in range (2, limit):
		factMap = {}
		for prime in primes:
			factMap[prime] = 0
		fact = factors(i)
		for j in fact:
			factMap[j] += 1
		factMaps.append(factMap)

	finalMap = {}
	for prime in primes:
		finalMap[prime] = 0

	for factMap in factMaps:
		for prime in primes:
			finalMap[prime] = max(finalMap[prime], factMap[prime])

	product = 1
	for prime in primes:
		product *= math.pow(prime, finalMap[prime])
	return math.trunc(product)

print(p5(10))

