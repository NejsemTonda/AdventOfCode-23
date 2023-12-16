lines = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

with open('input', 'r') as file:
	lines = file.read()



lines = lines.strip().split('\n')

def get_energized(beams, lines):
	energized = [["."]*len(lines[0]) for _ in range(len(lines))]
	
	visited = set()
	while beams != []:
		(x,y), (dx,dy) = beams.pop()
		if y >= len(lines) or x >= len(lines[0]) or y < 0 or x < 0:
			continue
	
		if ((x,y), (dx,dy)) in visited:
			continue
	
		energized[y][x] = "#"
		char = lines[y][x] 
		if char == ".":
			beams.append(((x+dx, y+dy), (dx, dy)))
	
		elif char == "-":
			if abs(dx) > 0: 
				beams.append(((x+dx, y+dy), (dx, dy)))
			else:
				beams.append(((x-1, y), (-1,0)))
				beams.append(((x+1, y), (1,0)))
	
		elif char == "|":
			if abs(dy) > 0: 
				beams.append(((x+dx, y+dy), (dx, dy)))
			else:
				beams.append(((x, y-1), (0,-1)))
				beams.append(((x, y+1), (0,1)))
	
		elif char == "\\":
			if dx == 1: 
				beams.append(((x, y+1), (0, 1)))
	
			elif dx == -1: 
				beams.append(((x, y-1), (0, -1)))
	
			elif dy == 1: 
				beams.append(((x+1, y), (1, 0)))
	
			elif dy == -1: 
				beams.append(((x-1, y), (-1, 0)))
	
		elif char == "/":
			if dx == 1: 
				beams.append(((x, y-1), (0, -1)))
	
			elif dx == -1: 
				beams.append(((x, y+1), (0, 1)))
	
			elif dy == 1: 
				beams.append(((x-1, y), (-1, 0)))
	
			elif dy == -1: 
				beams.append(((x+1, y), (1, 0)))
	
		visited.add(((x,y),(dx,dy)))
	
		#`print()
		#`print("\n".join(map("".join, energized)))
		
	return sum(map(lambda x: x.count("#"), energized))


possible_starts = []

for i in range(len(lines[0])):
	possible_starts.append(((i,0), (0,1)))

for i in range(len(lines[0])):
	possible_starts.append(((len(lines[0])-i-1,len(lines)-1), (0,-1)))

for i in range(len(lines)):
	possible_starts.append(((0,i), (1,0)))

for i in range(len(lines)):
	possible_starts.append(((len(lines)-1,len(lines[0])-i-1), (-1,0)))


print(max(map(lambda x: get_energized([x], lines), possible_starts)))
