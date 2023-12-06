import time
from itertools import chain
from dataclasses import dataclass
import numpy as np
import numba
import multiprocessing
from functools import partial
from tqdm import tqdm

with open("input", 'r') as file:
	lines = file.read().strip().split('\n')


_lines = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".strip().split('\n')



def parse(lines):
	maps = []
	seeds = list(map(int, lines[0].split(":")[1].strip().split(" ")))

	local_map = []
	for line in lines[2:]:
		if line == "":
			maps.append(local_map)
			local_map=[]
			continue

		if "map" in line:
			continue
		
		dst_start, src_start, l = map(int, line.split())
		local_map.append((src_start, dst_start, l))


	maps.append(local_map)
	return seeds, maps

			
e = 0.01
seeds, maps = parse(lines)
seeds = [(seeds[2*i], seeds[2*i]+seeds[2*i+1]) for i in range(len(seeds)//2)]


seed = seeds[0]
s = [seed]
s = seeds
	
for local_map in maps:
	new = []
	while len(s) > 0:
		interval = s.pop()
		ss,se = interval
		for mss, mds, l in local_map:
			mse = mss+l
			mde = mds+l
			if se < mss:
				continue
			if ss > mse:
				continue
			
			if mss <= ss <= mse and mss <= se <= mse:
				new.append((ss-mss+mds, se-mss+mds))
				break
		
			elif mss <= ss < mse and se > mse:
				new.append((ss-mss+mds, mde))
				s.append((mse, se))
				break
		
			elif ss < mss and mss < se <= mse:
				new.append((mds, se-mss+mds))
				s.append((ss, mss))
				break
		else:
			new.append(interval)
	s = new

print(min(s))
