
b = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.  """
b = b.strip().split('\n')

a = """
#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
a = a.strip().split('\n')

with open("input", 'r') as file:
	lines = file.read()

inputs = map(lambda x: x.strip().split('\n'), lines.split("\n\n"))


def t(s):
	return [''.join(x) for x in zip(*reversed(s))]

def transpose(s):
	return t(t(t(s)))


def get_idxs(s):
	idxs = []
	for i in range(1,len(s[0])):
		for line in s:
			if not (line[:i].endswith(line[i:][::-1]) or line[i:][::-1].endswith(line[:i])):
				break
	
		else:
			idxs.append(i)

	return idxs


r = sum(map(lambda x: sum(get_idxs(x)) + 100*sum(get_idxs(transpose(x))), inputs))
print(r)


