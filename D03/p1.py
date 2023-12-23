def is_symbol(c):
    return not (c.isdigit() or c == '.' or c == '\n')

def adj(M, i, j):
    H = len(M)
    if i >= 0 and j >= 0 and is_symbol(M[i-1][j-1]):
        return True
    if i >= 0 and is_symbol(M[i-1][j]):
        return True
    if i >= 0 and is_symbol(M[i-1][j+1]):
        return True
    if j >= 0 and is_symbol(M[i][j-1]):
        return True
    if is_symbol(M[i][j+1]):
        return True
    if i+1 < H and j > 0 and is_symbol(M[i+1][j-1]):
        return True
    if i+1 < H and is_symbol(M[i+1][j]):
        return True
    if i+1 < H and is_symbol(M[i+1][j+1]):
        return True
    return False

M = open('input').readlines()
W = len(M[0])
H = len(M)
nb, b, res = '', 0, 0
for i in range(H):
    for j in range(W):
        c = M[i][j]
        if c == '\n':
            continue
        if c.isdigit():
            nb += c
            if adj(M, i, j):
                b += 1
        elif nb != '':
            if b > 0:
                res += int(nb)
            nb = ''
            b = 0
print(res)
