from itertools import combinations
lines = """
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""
with open('input', 'r') as file:
	lines = file.read()

lines = lines.strip().split('\n')
print('\n'.join(lines))


def get_empty(s):
	rows = []
	columns = []
	for i,l in enumerate(s):
		if not '#' in l:
			rows.append(i)	

	for i in range(len(s[0])):
		if not '#' in [l[i] for l in s]:
			columns.append(i)

	return rows, columns


rows, columns = get_empty(lines)
N = 999999


def get_galaxies_pos(s):
	pos = []
	for y,l in enumerate(s):
		for x,c in enumerate(l):
			if c == "#":
				pos.append((x,y))

	return pos


cum = 0
pos = get_galaxies_pos(lines)


for g1, g2 in combinations(pos, 2):
	x_crossings = 0
	for c in columns:
		if min(g1[0], g2[0]) < c < max(g1[0], g2[0]):
			x_crossings += 1

	y_crossings = 0
	for r in rows:
		if min(g1[1], g2[1]) < r < max(g1[1], g2[1]):
			y_crossings += 1

	cum += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + N*(y_crossings+x_crossings)

print(cum)

