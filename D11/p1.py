import numpy as np

INPUT_FILE = 'input_test'

inp = open(INPUT_FILE).readlines()
for i in range(len(inp)):
    inp[i] = list(inp[i].replace('.', '0').replace('#', '1').strip())

arr = np.array(inp, dtype=np.int8)

i = 0
while i < arr.shape[0]:
    if not arr[i,:].any():
        arr = np.insert(arr, i, [0] * arr.shape[1], axis=0)
        i += 1
    i += 1

i = 0
while i < arr.shape[1]:
    if not arr[:,i].any():
        arr = np.insert(arr, i, [0] * arr.shape[0], axis=1)
        i += 1
    i += 1

def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

assert dist(0, 4, 10, 9) == 15
assert dist(2, 0, 7, 12) == 17
assert dist(11, 0, 11, 5) == 5

l = []

for (x, y), value in np.ndenumerate(arr):
    if value == 1:
        l.append((x,y))

res = 0
for i in range(len(l)):
    for j in range(i, len(l)):
        res += dist(l[i][0], l[i][1], l[j][0], l[j][1])

print(res)
