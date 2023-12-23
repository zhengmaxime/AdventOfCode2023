from math import lcm

INPUT_FILE = 'input'

# %%
def get_next(instr: str):
    i = 0
    l = len(instr)
    while True:
        yield instr[i % l]
        i += 1

# %%

lines = open(INPUT_FILE).readlines()

instr = lines[0].strip()
d = dict()

test_z = []
for i in range(2, len(lines)):
    line = lines[i].replace('=', ' ').replace('(', ' ').replace(')', ' ').replace(',', ' ')
    n1, n2, n3 = line.split()
    d[n1] = (n2, n3)

nb_steps = 0
g = get_next(instr)
n_cur_list = list(filter(lambda x: x.endswith('A'), d.keys()))


# %%
all_nb_steps = []
for i in range(len(n_cur_list)):
    n_cur = n_cur_list[i]
    n_next = ''
    nb_steps = 0
    while not n_cur.endswith('Z'):
        direction = g.__next__()
        #print(direction)
        if direction == 'L':
            n_next = d[n_cur][0]
        elif direction == 'R':
            n_next = d[n_cur][1]
        n_cur = n_next
        nb_steps += 1
        #print(n_cur)
    all_nb_steps.append(nb_steps)

print(all_nb_steps)
print(lcm(*all_nb_steps))