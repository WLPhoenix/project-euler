primes = []

import math
import sys

def findPrimes():
	limit = (2000000) #manual tuning tweek
	flags = [True] * limit
	flags[0] = flags[1] = False

	for(i, isprime) in enumerate(flags):
		if isprime:
			primes.append(i)
			for n in xrange(i, limit, i):		
				flags[n] = False

findPrimes()

sumPrimes = 0
for(i, prime) in enumerate(primes):
	if prime < 2000000:
		sumPrimes += prime
	else:
		print("Target reached.")
		break
print(sumPrimes)