r=0
for g in open('f'):
 d={'r':0,'g':0,'b':0}
 for e in g[5:].split(':')[1].replace(';',',').split(','):
  n,c=e.split()
  d[c[0]]=max(int(n),d[c[0]])
 r+=d['r']*d['g']*d['b']
print(r)
