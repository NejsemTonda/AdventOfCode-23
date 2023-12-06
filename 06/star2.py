lines = """
Time:        56     71     79     99
Distance:   334   1135   1350   2430
""".strip().split("\n")



t = int("".join(lines[0].split(':')[1].strip().split()))
d = int("".join(lines[1].split(':')[1].strip().split()))

ways = 0
for w in range(1,t):
	if (t-w)*w > d:
		ways += 1
	if w%1000000 == 0:
		print(w/t)

print(ways)
