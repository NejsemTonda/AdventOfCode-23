def printl(lines):
	print('\n'.join(map(lambda x: "".join(x), lines)))

lines = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

with open("input", 'r') as file:
    lines = file.read()

lines = lines.strip().split('\n')


dug = [["." for _ in range(400)] for _ in range(400)]

directions = {
    'R' : [1,0],
    'L' : [-1,0],
    'D' : [0,-1],
    'U' : [0,1],
}

digger = [0,0]
dug[digger[1]][digger[0]] = "#"

max_x = -10000
min_x = 10000

max_y = -10000
min_y = 10000
for l in lines:
    tokens = l.split(' ')
    d = directions[tokens[0]]
    for _ in range(int(tokens[1])):
        digger[0] += d[0] 
        digger[1] += d[1] 
        min_x = min(digger[0], min_x)
        max_x = max(digger[0], max_x)
        min_y = min(digger[1], min_y)
        max_y = max(digger[1], max_y)

digger = [-min_x, -min_y]
dim_x = max_x-min_x+1
dim_y = max_y-min_y+1
dug = [["." for _ in range(dim_x)] for _ in range(dim_y)]

for l in lines:
    tokens = l.split(' ')
    d = directions[tokens[0]]
    for _ in range(int(tokens[1])):
        digger[0] += d[0] 
        digger[1] += d[1] 

        dug[digger[1]][digger[0]] = "#"


printl(dug)

q = [(dim_x//2,dim_y//2)]
#dug[q[0][1]][q[0][0]] = "C"

while len(q) > 0:
    x,y = q.pop()
    if x >= len(dug[0]) or y >= len(dug):
        continue

    if dug[y][x] == "#":
        continue
    
    dug[y][x] = "#"
    for d in directions.values():
        q.append((x+d[0], y+d[1]))


printl(dug)

print(sum([line.count('#') for line in dug]))
