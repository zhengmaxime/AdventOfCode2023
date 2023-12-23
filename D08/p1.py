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

for i in range(2, len(lines)):
    line = lines[i].replace('=', ' ').replace('(', ' ').replace(')', ' ').replace(',', ' ')
    n1, n2, n3 = line.split()
    d[n1] = (n2, n3)

print(d, instr)

nb_steps = 0
g = get_next(instr)
n_cur = 'AAA'
while n_cur != 'ZZZ':
    direction = g.__next__() 
    #print(direction)
    if direction == 'L':
        n_next = d[n_cur][0]
    elif direction == 'R':
        n_next = d[n_cur][1]
    n_cur = n_next
    nb_steps += 1

print(nb_steps)