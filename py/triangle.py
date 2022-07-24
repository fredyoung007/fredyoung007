def print_numbers_triangle(n):
	for i in range(0, n):
		s = ""
		for j in range(0, i+1):
			s += str(j+1)
		print(s.rjust(n))
print_numbers_triangle(8)
