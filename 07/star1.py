sorter = {
	'A' : 13, 
	'K' : 12, 
	'Q' : 11,  
	'J' : 10,  
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

	values = sorted([v for k,v in counts.items()])[::-1]
	hand_value = [sorter[c] for c in s]

	return (values, hand_value)
	

lines ="""
2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41
"""
with open("input", 'r') as file:
	lines = file.read()
lines = lines.strip().split('\n')

lines = [(h, int(r)) for h,r in map(lambda x: x.split(), lines)]

wins = sorted(lines, key= lambda h : score(h[0]))

print(sum([k*v for k,v in zip([s for _, s in wins], range(1, len(wins)+1))]))

