def is_symbol(c):
    return c == '*'

def adj(M, i, j):
    H = len(M)
    if i >= 0 and j >= 0 and is_symbol(M[i-1][j-1]):
        return (i-1,j-1)
    if i >= 0 and is_symbol(M[i-1][j]):
        return (i-1,j)
    if i >= 0 and is_symbol(M[i-1][j+1]):
        return (i-1,j+1)
    if j >= 0 and is_symbol(M[i][j-1]):
        return (i,j-1)
    if is_symbol(M[i][j+1]):
        return (i,j+1)
    if i+1 < H and j > 0 and is_symbol(M[i+1][j-1]):
        return (i+1,j-1)
    if i+1 < H and is_symbol(M[i+1][j]):
        return (i+1,j)
    if i+1 < H and is_symbol(M[i+1][j+1]):
        return (i+1,j+1)
    return (-1,-1)

M = open('input').readlines()
W = len(M[0])
H = len(M)

d = {}
for i in range(H):
    for j in range(W):
        if M[i][j] == '*':
            d[(i,j)] = []

nb, xx, yy, res = '', -1, -1, 0
for i in range(H):
    for j in range(W):
        c = M[i][j]
        if c == '\n':
            continue
        if c.isdigit():
            nb += c
            x, y = adj(M, i, j)
            if x != -1:
                xx, yy = x, y
        elif nb != '':
            if xx != -1:
                d[(xx,yy)].append(int(nb))
            nb = ''
            xx, yy = -1, -1
for value in d.values():
    if len(value) == 2:
        res += value[0] * value[1]
print(res)
