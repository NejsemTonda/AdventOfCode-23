lines = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

with open("input", 'r') as file:
	lines = file.read()

lines = list(map(lambda x : ["#"] + list(x) + ["#"], lines.strip().split('\n')))
lines = [["#"]*len(lines[0])] + lines + [["#"]*len(lines[0])]
for l in lines:
	print("".join(l))

print()
print()

def north(s):
	for i in range(len(s[0])):
		rocks = 0
		for i2, line in enumerate(reversed(s)):
			if line[i] == "O":
				line[i] = "."
				rocks += 1
	
			elif line[i] == "#":
				if rocks > 0:
					for r in range(rocks):
						s[-i2+r][i] = "O"
					rocks = 0




def west(s):
	for line in s:
		rocks = 0
		for i2, c in enumerate(reversed(line)):
			if c == "O":
				line[-i2-1] = "."
				rocks += 1
	
			elif c == "#":
				if rocks > 0:
					for r in range(rocks):
						line[-i2+r] = "O"
					rocks = 0


def south(s):
	for i in range(len(s[0])):
		rocks = 0
		for i2, line in enumerate(s):
			if line[i] == "O":
				line[i] = "."
				rocks += 1
	
			elif line[i] == "#":
				if rocks > 0:
					for r in range(rocks):
						s[i2-r-1][i] = "O"
					rocks = 0


def east(s):
	for line in s:
		rocks = 0
		for i2, c in enumerate(line):
			if c == "O":
				line[i2] = "."
				rocks += 1
	
			elif c == "#":
				if rocks > 0:
					for r in range(rocks):
						line[i2-r-1] = "O"
					rocks = 0

def get_load(s):
	load = 0
	for i, line in enumerate(s):
		stones = line.count("O")
		#print(line, len(s)-i-1, stones)
		load += stones*(len(s)-i-1)

	return load



	return load



s = '\n'.join(map("".join, lines))
seen = [s]
loads = [get_load(lines)]
i = 0 
while True:
	north(lines)
	west(lines)
	south(lines)
	east(lines)
	s = '\n'.join(map("".join, lines))
	print(get_load(lines))
	if s in seen:
		break
	seen.append(s)
	loads.append(get_load(lines))
	i += 1

print(get_load(lines))
print(loads)

s = '\n'.join(map("".join, lines))
first = seen.index(s)

print(first)
print(i)


print()
print()
print()
print(loads[(1_000_000_000 - first) % (first-i-1)])

