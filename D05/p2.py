from collections import defaultdict

DEBUG = False
INPUT_FILE = 'input'

def printb(*s):
    if DEBUG:
        print(s)

input_lines = open(INPUT_FILE).readlines()
seeds_line = input_lines[0][6:]
seeds = seeds_line.split()
seeds = [ int(x) for x in seeds ]

"""
Bruteforce works with example input only :)
new_seeds = []
for i in range(0, len(seeds), 2):
    for k in range(seeds[i], seeds[i] + seeds[i + 1]):
        new_seeds.append(k)
printb(new_seeds)
seeds = new_seeds
"""

new_seeds = []
for i in range(0, len(seeds), 2):
    new_seeds.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
seeds = new_seeds
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

def get_location_number(seeds):
    for map_category in map_order:
        printb(map_category, seeds)
        next_category_seeds = []
        for m in d[map_category]:
            next_map_seeds = []
            dest, src, range_length = m
            delta, i1, i2 = dest - src, src, src + range_length - 1 # 98+range=2 => [98, 99] or [98, 100[
            printb(map_category, i1, i2, delta, seeds)
            for seed_b, seed_e in seeds:
                if i1 <= seed_b <= seed_e <= i2:
                    next_category_seeds.append((seed_b + delta, seed_e + delta))
                elif seed_b < i1 < i2 < seed_e:
                    next_category_seeds.append((i1 + delta, i2 + delta))
                    next_map_seeds.append((seed_b, i1 - 1))
                    next_map_seeds.append((i2 + 1, seed_e))
                elif seed_b < i1 <= seed_e <= i2:
                    next_category_seeds.append((i1 + delta, seed_e + delta))
                    next_map_seeds.append((seed_b, i1 - 1))
                elif i1 <= seed_b <= i2 < seed_e:
                    next_category_seeds.append((seed_b + delta, i2 + delta))
                    next_map_seeds.append((i2 + 1, seed_e))
                elif seed_b <= seed_e < i1 or i2 < seed_b <= seed_e:
                    next_map_seeds.append((seed_b, seed_e))
            seeds = next_map_seeds
        seeds = next_category_seeds + next_map_seeds
    return seeds

print(min(min(get_location_number(seeds))))
