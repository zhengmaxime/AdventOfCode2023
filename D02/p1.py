d,r={'r':12,'g':13,'b':14},0
for g in open('f'):
 i,k=g[5:].split(':')
 for e in k.replace(';',',').split(','):
  n,c=e.split()
  if int(n)>d[c[0]]:
   i=0
 r+=int(i)
print(r)