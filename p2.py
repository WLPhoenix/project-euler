sum = 0
max = 4000000
a, b = 0, 1
while(a < max):
	if a % 2 == 0:
		sum += a
	a, b = b, a+b
print sum	