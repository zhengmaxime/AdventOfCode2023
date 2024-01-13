from collections import defaultdict

INPUT_FILE = 'input'

input_lines = open(INPUT_FILE).readlines()

seeds_line = input_lines[0][6:]
seeds = seeds_line.split()
seeds = [ int(x) for x in seeds ]

d = defaultdict(list)
step_name = None

for line in input_lines:
    line = line.strip()
    if line == '':
        step_name = None
        continue
    if step_name is not None:
        numbers = line.split()
        numbers = [ int(x) for x in numbers ]
        d[step_name].append(numbers)
    elif line.endswith('map:'):
        step_name = line[:-5]

map_order = ['seed-to-soil',
             'soil-to-fertilizer',
             'fertilizer-to-water',
             'water-to-light',
             'light-to-temperature',
             'temperature-to-humidity',
             'humidity-to-location']

def get_location_number(seed):
    for map_category in map_order:
        for m in d[map_category]:
            dest, src, rnge = m
            delta = dest - src
            if seed >= src and seed <= src + rnge:
                seed += delta
                break
    return seed

res = [ get_location_number(seed) for seed in seeds]
print(min(res))
