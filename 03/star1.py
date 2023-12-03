with open("input", 'r') as file:
	lines = file.read()

#lines = filter(lambda c: not c.isdigit() and c != ".", lines)
#print(list(set(lines)))
#quit()

sp = ['-', '*', '=', '+',  '/', '#', '$', '%', '@', '&']

#lines = """
#12.......*..
#+.........34
#.......-12..
#..78........
#..*....60...
#78.........9
#.5.....23..$
#8...90*12...
#............
#2.2......12.
#.*.........*
#1.1..503+.56""".strip()
lines = lines.split('\n')
special = []

for li, line in enumerate(lines):
	for ci, c in enumerate(line):
		if c in sp:
			special.append((li, ci))

print(special)
	
s = 0
for li, line in enumerate(lines):
	line += "."
	digit = ""
	valid = False
	for ci, c in enumerate(line):
		if c.isdigit():
			if digit == "":
				if (li-1,ci-1) in special or (li, ci-1) in special or (li+1, ci-1) in special:
					valid = True
			digit += c
			if (li-1, ci) in special or (li+1, ci) in special:
				valid = True

		else:
			if digit != "":
				if (li-1,ci) in special or (li, ci) in special or (li+1, ci) in special:
					valid = True
				
				print(f"{digit} is {valid}")
				if valid:
					s += int(digit)
				digit = ""
				valid = False

print(s)
