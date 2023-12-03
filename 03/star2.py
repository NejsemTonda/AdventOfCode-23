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
stars = {}

for li, line in enumerate(lines):
	for ci, c in enumerate(line):
		if c == "*":
			stars[(li, ci)] = []

print(special)
	
for li, line in enumerate(lines):
	line += "."
	digit = ""
	suroundings = []
	for ci, c in enumerate(line):
		if c.isdigit():
			if digit == "":
				suroundings.append((li-1,ci-1))
				suroundings.append((li, ci-1))
				suroundings.append((li+1, ci-1))
			digit += c
			suroundings.append((li-1, ci))
			suroundings.append((li+1, ci))

		else:
			if digit != "":
				suroundings.append((li-1,ci))
				suroundings.append((li, ci))
				suroundings.append((li+1, ci))

				for s in suroundings:
					if s in stars:
						stars[s].append(int(digit))
					
				
				digit = ""
				suroundings = []

print(sum([v[0]*v[1] for _,v in stars.items() if len(v) == 2]))
