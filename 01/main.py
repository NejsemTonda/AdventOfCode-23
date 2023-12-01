# ------------------------------First Star------------------------------
with open("input", 'r') as file:
	lines = file.read().split()

s = 0
for line in lines:
	digits = [c for c in line if c.isdigit()]
	first_last = digits[0]+digits[-1]
	s += int(first_last)

print(s)



# ------------------------------Second Star------------------------------
with open("input", 'r') as file:
	lines = file.read().split()


def get_first(s):
	words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	nums = list(map(str, (range(1,10))))

	for i in range(len(s)):
		if s[i] in nums:
			return int(s[i])
		for k in range(len(max(words, key = lambda x: len(x)))+1):
			if s[i:i+k] in words:
				return words.index(s[i:i+k])+1 

def get_last(s):
	s = s[::-1]
	words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	words = [w[::-1] for w in words]
	nums = list(map(str, (range(1,10))))

	for i in range(len(s)):
		if s[i] in nums:
			return int(s[i])
		for k in range(len(max(words, key = lambda x: len(x)))+1):
			if s[i:i+k] in words:
				return words.index(s[i:i+k])+1 



s = 0
for l in lines:
	s += get_first(l)*10+get_last(lk

print(s)

