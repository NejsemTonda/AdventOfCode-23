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
	
	return ",".join(map(str,actual)) == res

def recur(springs, res):
	if "?" in springs:
		i = springs.index("?")
		#springs[i] = "#"
		r1 = recur(springs[:i]+["#"]+springs[i+1:], res)

		#springs[i] = "."
		r2 = recur(springs[:i]+["."]+springs[i+1:], res)

		return r1+r2

	return 1 if check_line(springs, res) else 0
	
s = 0
for line in lines:
	springs, res = line.split(" ") 
	springs = list(springs) + ["."]
	k = recur(springs, res)
	print(f"{line} ---> {k}")
	s += k

print(s)
