primes = []

import math
import sys

def findPrimes(limit_index):
	limit = (sys.maxint>>14) #manual tuning tweek
	flags = [True] * limit
	flags[0] = flags[1] = False

	for(i, isprime) in enumerate(flags):
		if isprime:
			primes.append(i)
			for n in xrange(i, limit, i):		
				flags[n] = False
		if len(primes) == limit_index:
			return i
	print(max(primes))
	print("Go bigger.")

print(findPrimes(10001))