r=0
for g in open('f'):
 w,m=g.split(':')[1].split('|')
 s=set(w.split())
 c=len(s&(set(m.split())))-1
 r+=int(2**c)
print(r)
