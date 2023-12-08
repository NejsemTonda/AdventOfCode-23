import math

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

lines = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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


# this function is slow, I dont want to optimise it because this day was poorly formulated...
def get_cycle_len(n, instructions, network):
	visited = []
	i = 0
	znode = None
	while not (n, i%len(instructions)) in visited:
		#if n[-1] == "Z":
		#	znode = i
		visited.append((n, i%len(instructions)))
		n = network[n][0 if instructions[i%len(instructions)] == "L" else 1]
		i += 1

	cycle_len  = len(visited) - visited.index((n, i%len(instructions)))
	#cycle_start  = {visited.index((n, i%len(instructions)))} ---------> Dont need those, the quiestion if formulated really strange
	return cycle_len


lines = lines.strip().split('\n')
instructions = lines[0]
network_s = lines[2:]

network = get_network(network_s)

i = 0
nodes = [n for n in network.keys() if n[-1] == "A"]

print(math.lcm(*[get_cycle_len(n, instructions, network) for n in nodes]))
