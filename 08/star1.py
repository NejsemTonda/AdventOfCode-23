import time

lines = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

lines = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

with open('input', 'r') as file:
	lines = file.read()


def get_network(lines):
	d = {}
	for l in lines:
		node, paths = map(lambda x: x.strip(), l.split("="))
		L, R = map(lambda x: x.strip(), paths.replace("(", "").replace(")", "").split(','))
		d[node] = (L,R)

	return d


lines = lines.strip().split('\n')
instructions = lines[0]
network_s = lines[2:]

network = get_network(network_s)
print(network)

i = 0
node = "AAA"
while node != "ZZZ":
	node = network[node][0 if instructions[i%len(instructions)] == "L" else 1]
	i += 1
	print(node)

print(i)

