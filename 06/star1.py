lines = """
Time:        56     71     79     99
Distance:   334   1135   1350   2430
""".strip().split("\n")

times = list(map(int, lines[0].split(':')[1].strip().split()))
distances = list(map(int, lines[1].split(':')[1].strip().split()))


res = 1
for t,d in zip(times, distances):
	ways = 0
	for w in range(1,t):
		if (t-w)*w > d:
			ways += 1

	res *= ways

print(res)
