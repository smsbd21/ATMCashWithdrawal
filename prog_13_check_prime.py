num = int(input("Check for prime:"))
if num > 1:
	for i in range(2, int(num/2)):
		if num % i == 0:
			print(num, 'is not prime')
			break
	else:
		print(num, 'is prime')
else:
	print(num, "neither prime nor composite")