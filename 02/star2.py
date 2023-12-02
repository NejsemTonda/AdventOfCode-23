
with open('input', 'r') as file:
	lines = file.read().strip()

lines = lines.split('\n')


def process_line(line):
	maxes = {
		'red' : 0,
		'green' : 0,
		'blue' : 0,
	} 
	draws = line.split(':')[1].split(';')
	for draw in draws:
		for info in draw.split(','):
			tokens = info.split()
			count = int(tokens[0])
			color = tokens[1]
			maxes[color] = max(maxes[color], count)
	k = 1
	for v in maxes.values():
		k *= v

	return k

print(sum(map(process_line, lines)))
