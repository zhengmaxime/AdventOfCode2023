r,l=0,open('f').readlines()
for g in l:
    w, m = g.split(':')[1].split('|')
    s = set()
    for n in w.split():
        s.add(n)
    c = 0
    for n in m.split():
        if n in s:
            c += 1
    if c > 0:
        r += 2 ** ((int(c)-1))
print(r)
