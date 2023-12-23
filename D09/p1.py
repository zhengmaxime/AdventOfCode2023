INPUT_FILE = 'input'

def process_line(l):
    res = []
    for i in range(1, len(l)):
        res.append(l[i] - l[i-1])
    return res

def is_zero(l):
    return min(l) == max(l) == 0

def process_sequence_down(line):
    lines = [line]
    while not is_zero(line):
        diffs = process_line(line)
        lines.append(diffs)
        line = diffs
    return lines

def process_sequence_up(ll):
    for i in range(1, len(ll)):
        l1 = ll[-i]
        l2 = ll[-i-1]
        l1.append(l1[-1])
        l2.append(l2[-1] + l1[-1])
    return ll[0][-1]

res = []
for line in open(INPUT_FILE):
    l = line.split()
    l = [ int(x) for x in l ]
    ll = process_sequence_down(l)
    res.append(process_sequence_up(ll))
print(sum(res))