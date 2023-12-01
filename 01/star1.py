with open("input", 'r') as file:
	lines = file.read().split()

s = 0
for line in lines:
	digits = [c for c in line if c.isdigit()]
	first_last = digits[0]+digits[-1]
	s += int(first_last)

print(s)


