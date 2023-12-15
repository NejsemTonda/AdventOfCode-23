
lines = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
with open("input", 'r') as file:
	lines = file.read()

lines = lines.strip().split(',')


def HASH(s):
	v = 0 
	for c in s:
		v = ((v+ord(c))*17) % 256
	return v

print(sum(map(HASH, lines)))

