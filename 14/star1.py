lines = """
##########
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

lines = lines.strip().split('\n')
load = 0

for i in range(len(lines[0])):
	rocks = 0
	for i2, line in enumerate(reversed(lines)):
		if line[i] == "O":
			rocks += 1

		elif line[i] == "#":
			if rocks > 0:
				load += rocks*(rocks-1)/2 + (i2-rocks+1)*rocks
				rocks = 0



print(load)
