from functools import cache
import time
lines = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
with open("input", 'r') as file:
	lines = file.read()

lines = lines.strip().split('\n')

def check_line(springs, res):
	i = 0
	actual = []
	while i < len(springs):
		if springs[i] == "#":
			g = 0
			while springs[i] == "#":
				g += 1
				i += 1

			actual.append(g)

		i += 1
	
	return actual == res

@cache
def reduce(springs, res, hastags):
	if len(res) == 0:
		if "#" in springs:
			return 0
		return 1

	if len(springs) == 0:
		return 0

	if springs[0] == ".":
		if hastags != 0:
			res0 = int(res.split(',')[0])
			if hastags == res0:
				return reduce(springs[1:], res[len(str(res0))+1:], 0)
			else:
				return 0
		else:
			return reduce(springs[1:], res, 0)

	elif springs[0] == "#":
		return reduce(springs[1:], res, hastags+1)

	elif springs[0] == "?":
		r1 = reduce("#"+springs[1:], res, hastags)
		r2 = reduce("."+springs[1:], res, hastags)
		return r1 + r2

start = time.time()
s = 0
for line in lines:
	print(line, end = "\r")
	springs, res = line.split(" ") 
	springs = "?".join([springs]*5)
	springs += "."
	res = ",".join([res]*5)
	k = reduce(springs, res, 0)
	print(f"{line} ---> {k}")
	s += k

print(s)
print(time.time() - start)
