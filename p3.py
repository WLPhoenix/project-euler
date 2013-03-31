import math

primes = []
def findPrimes(limit):
	limit = math.trunc(math.sqrt(limit))+1
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

def p3(target):
	findPrimes(target)
	target_factors = factors(target)
	print(max(target_factors))

p3(600851475143)
