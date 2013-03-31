import math

def sumSquare(limit):
	sqSum = 0
	for i in range(1, limit+1):
		sqSum += i*i
	return math.trunc(sqSum)

def squareSum(limit):
	limSum = (limit * (limit+1))>>1
	return limSum * limSum

def p6(limit):
	return abs(sumSquare(limit) - squareSum(limit))

print(p6(100))