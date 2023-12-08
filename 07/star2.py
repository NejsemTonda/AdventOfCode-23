sorter = {
	'A' : 13, 
	'K' : 12, 
	'Q' : 11,  
	'J' : 0,  
	'T' : 9,  
	'9' : 8,  
	'8' : 7,  
	'7' : 6,  
	'6' : 5,  
	'5' : 4,  
	'4' : 3,  
	'3' : 2,  
	'2' : 1, 
}

def score(s):
	counts = {}
	
	for c in s:
		counts[c] = counts.get(c, 0) + 1 
	values = sorted([v for _,v in counts.items()])[::-1]

	return values

# inefficient, but fast enough
def recur(s):
	if not "J" in s:
		return score(s)
	
	else:
		index = s.index("J")
		m = []
		s = s[:]
		for c in sorter.keys():
			if c == "J":
				continue 
			s[index] = c 
			m = max(recur(s), m)	
		return m

def eval_hand(s):
	max_s = recur(list(s[:]))
	hand_value = [sorter[c] for c in s]
	return (max_s, hand_value)
	

with open("input", 'r') as file:
	lines = file.read()

lines = lines.strip().split('\n')

lines = [(h, int(r)) for h,r in map(lambda x: x.split(), lines)]

wins = sorted(lines, key= lambda h : eval_hand(h[0]))

print(sum([k*v for k,v in zip([s for _, s in wins], range(1, len(wins)+1))]))

