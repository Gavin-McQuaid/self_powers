i = 1
total = 0
while i <= 1000:
	total += i ** i
	i += 1
total = str(total)
print total[-10:]
