import numpy as np

INPUT_FILE = 'input'

inp = open(INPUT_FILE).readlines()
for i in range(len(inp)):
    inp[i] = list(inp[i].replace('.', '0').replace('#', '1').strip())

arr = np.array(inp, dtype=np.int8)

def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

assert dist(0, 4, 10, 9) == 15
assert dist(2, 0, 7, 12) == 17
assert dist(11, 0, 11, 5) == 5

lx = []
ly = []

for (x, y), value in np.ndenumerate(arr):
    if value == 1:
        lx.append(x)
        ly.append(y)

N = 1_000_000 - 1

i = 0
c = 0
while i < arr.shape[0]:
    if not arr[i,:].any():
        lx = [ x + N if x - c * N > i else x for x in lx]
        c += 1
    i += 1

i = 0
c = 0
while i < arr.shape[1]:
    if not arr[:,i].any():
        ly = [ y + N if y - c * N > i else y for y in ly]
        c += 1
    i += 1

#print(list(zip(lx, ly)))

res = 0
for i in range(len(lx)):
    for j in range(i, len(lx)):
        res += dist(lx[i], ly[i], lx[j], ly[j])

print(res)
