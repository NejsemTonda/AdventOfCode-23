import time

lines = """
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
"""


with open("input", 'r') as file:
	lines = file.read()
	
def rep(s):
	return s.replace("F", "╭").replace("7", "╮").replace('J', "╯").replace("L","╰")
lines = lines.strip().split('\n')
lines = ['.'*(len(lines[0])+2)] + ['.' + l + '.' for l in lines] + ['.'*(len(lines[0])+2)]
print('\n'.join([rep(l) for l in lines]))
pipes = list(map(list, lines))

def find_S(pipes):
	for i,line in enumerate(pipes):
		if "S" in line:
			return (i,line.index("S"))
	raise ValueError("No S")


distances = [[-1] * len(pipes[0]) for _ in range(len(pipes))]
dirs = [(0,1), (-1,0), (0,-1), (1,0)]

s = find_S(pipes)
q = [(s, (0,0))]

visited = []
while len(q) > 0:
	(x,y), (fx, fy) = q.pop(0)
	visited.append((x,y))
	char = pipes[x][y]

	if char == "S":
		for (dx,dy), p in zip(dirs, [["J","-","7"], ["|", "7", "F"], ["-", "F", "L"], ["|", "L", "J"]]):
			next_char = pipes[x+dx][y+dy]
			if next_char in p:
				distances[x][y] = 0
				q.append(((x+dx,y+dy), (x,y)))

	if distances[x][y] < 0:
		distances[x][y] = distances[fx][fy]+1
		if char == "-":
			q.append(((x, y+(y-fy)), (x,y)))

		elif char == "|":
			q.append(((x+(x-fx), y), (x,y)))

		if char == "F" or char == "J":
			q.append(((x-(y-fy), y-(x-fx)), (x,y)))

		if char == "L" or char == "7":
			q.append(((x+(y-fy), y+(x-fx)), (x,y)))


for x,l in enumerate(pipes):	
	for y in range(len(l)):
		if (x,y) not in visited:
			pipes[x][y] = "."
	
pipes[s[0]][s[1]] = "L"
print('\n'.join([''.join(l) for l in pipes]))

tiles = 0
for l in pipes:
	inside = False
	i = 0
	while i < len(l):
		if l[i] == "|":
			inside = not inside

		if l[i] == "F":
			i += 1
			while l[i] == "-":
				i += 1

			if l[i] == "7":
				pass
			if l[i] == "J":
				inside = not inside

		if l[i] == "L":
			i += 1
			while l[i] == "-":
				i += 1

			if l[i] == "J":
				pass
			if l[i] == "7":
				inside = not inside

		if l[i] == ".":
			tiles += 1 if inside else 0 	
			l[i] = "@" if inside else l[i]

		i += 1

print(tiles)
print('\n'.join([rep(''.join(l)) for l in pipes]))


