INPUT_FILE = 'input'

tks = open(INPUT_FILE).read().strip().split(',')

res = 0
for tk in tks:
    val = 0
    for c in tk:
        val += ord(c)
        val *= 17
        val = val % 256
    res += val

print(res)