import time

lines = """
..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""


_ines = """
.......
..7FJ..
..LS7..
..FJL..
.......
"""
_ines = """
........
.F7.....
SJL--7..
....LJ..
........
"""

with open("input", 'r') as file:
	lines = file.read()


lines = lines.strip().split('\n') 

pipes = list(map(list, lines))

def find_S(pipes):
	for i,line in enumerate(pipes):
		if "S" in line:
			return (i,line.index("S"))


distances = [[-1] * len(pipes[0]) for _ in range(len(pipes))]
dirs = [(0,1), (-1,0), (0,-1), (1,0)]

s = find_S(pipes)
q = [(s, (0,0))]

while len(q) > 0:
	(x,y), (fx, fy) = q.pop(0)
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

for d in distances:
	print("".join(map(str, d)))

print()
print(max([max(l) for l in distances]))



