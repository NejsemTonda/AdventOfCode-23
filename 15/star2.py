
lines = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
with open("input", 'r') as file:
	lines = file.read()

lines = lines.strip().split(',')


def HASH(s):
	v = 0 
	for c in s:
		v = ((v+ord(c))*17) % 256
	return v

boxes = [[] for _ in range(256)]

for cmd in lines:
	print(cmd)
	if "=" in cmd:
		tokens = cmd.split("=")
		s = tokens[0]
		n = int(tokens[1])
		box = boxes[HASH(s)]
		if s in [x[0] for x in box]:
			box[[x[0] for x in box].index(s)] = (tokens[0], n)
		else:
			box.append((tokens[0], n))

	elif "-" in cmd:
		s = cmd[:-1]
		box = boxes[HASH(s)]
		if s in [x[0] for x in box]:
			box.pop([x[0] for x in box].index(s))

s = 0
for i,box in enumerate(boxes):
	for i2,(_,p) in enumerate(box):
		s += (i2+1)*(i+1)*p

print(s)
