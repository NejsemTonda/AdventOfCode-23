maxes = {
	'red' : 12,
	'green' : 13,
	'blue' : 14,
} 

with open('input', 'r') as file:
	lines = file.read().strip()

lines = lines.split('\n')


def process_line(line):
	line = line.split(':')[1]
	draws = line.split(';')
	for draw in draws:
		for info in draw.split(','):
			tokens = info.split()
			count = int(tokens[0])
			color = tokens[1]
			if maxes[color] < count:
				return False
	return True

	
t = 0
for c,line in enumerate(lines):
	if process_line(line):
		t += c+1

print(t)
