with open("input", 'r') as file:
	lines = file.read().strip().split('\n')




#lines = """seeds: 79 14 55 13
#
#seed-to-soil map:
#50 98 2
#52 50 48
#
#soil-to-fertilizer map:
#0 15 37
#37 52 2
#39 0 15
#
#fertilizer-to-water map:
#49 53 8
#0 11 42
#42 0 7
#57 7 4
#
#water-to-light map:
#88 18 7
#18 25 70
#
#light-to-temperature map:
#45 77 23
#81 45 19
#68 64 13
#
#temperature-to-humidity map:
#0 69 1
#1 0 69
#
#humidity-to-location map:
#60 56 37
#56 93 4
#""".strip().split('\n')



def parse(lines):
	maps = []
	seeds = list(map(int, lines[0].split(":")[1].strip().split(" ")))

	local_map = []
	for line in lines[1:]:
		if line == "":
			maps.append(local_map)
			local_map=[]
			continue

		if "map" in line:
			continue
		
		dst_start, src_start, l = map(int, line.split())
		local_map.append((range(src_start, src_start+l), range(dst_start, dst_start+l)))

	maps.append(local_map)
		
	return seeds, maps
			
seeds, maps = parse(lines)

def plant(s, maps):
	for local_map in maps:
		for src, dst in local_map:
			if s in src:
				s = dst[src.index(s)]
				break
	return s

print(min(map(lambda x: plant(x, maps), seeds)))







