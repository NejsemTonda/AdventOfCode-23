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


directions = {
    'R' : (1,0),
    'L' : (-1,0),
    'D' : (0,-1),
    'U' : (0,1),
}

points = [(0,0)]
A = 0
error = 0
for line in lines:
    _, _, color = line.split()
    dx, dy = directions["RDLU"[int(color[-2:-1])]]
    l = int(color[2:-2], 16)
    error += l
    x,y = points[-1]
    points.append((x+l*dx, y+l*dy))

for i in range(len(points)):
    A += points[i][0] * (points[(i+1)%len(points)][1] - points[i-1][1])
A = abs(A//2)+error//2+1

print(A)
