
lines = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""
with open("input", 'r') as file:
    lines = file.read()

lines = lines.strip().split('\n')


workflows = {}
parts = []
ret = 0


parts = False
for line in lines:
    if line == "":
        parts = True
        continue

    if not parts:
        name = line[:line.index("{")]
        rules = line[line.index("{")+1:-1]
        rules = rules.split(",")
        ruleset = []
        for r in rules[:-1]:
            ruleset.append((r[0],int(r[2:r.index(":")]),(-1 if r[1] == "<" else 1), r[r.index(":")+1:]))
        default = rules[-1]
 
        workflows[name] = (ruleset, default)

    else:
        xmas = line[1:-1].split(",")
        xmas = list(map(lambda x: int(x[2:]), xmas))
        wf = "in"

        while wf not in "AR":
            rules, default = workflows[wf]
            for l, cond, sign, target in rules:
                value = xmas["xmas".index(l)] 
                if sign*cond < sign*value:
                    wf = target
                    break  

            else:
                wf = default
        ret += sum(xmas) if wf == "A" else 0

print(ret)


