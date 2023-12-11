
lines="""
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

with open("input", 'r') as file:
	lines = file.read()

lines = list(map(lambda x: list(map(int, x.split())), lines.strip().split('\n')))



def predict(l):
	difs = [l]
	while not all([x == 0 for x in difs[-1]]):
		new = []
		for i in range(len(difs[-1])-1):
			new.append(difs[-1][i+1] - difs[-1][i])

		difs.append(new)

	difs[-1].append(0)
	for i in range(len(difs)-2,-1, -1):
		difs[i].append(difs[i][-1]+difs[i+1][-1])

	return difs[0][-1]


print(sum([predict(l) for l in lines]))
