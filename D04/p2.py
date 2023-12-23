l=open('f').readlines()
i,n=0,[1]*len(l)
for g in l:
 w,m=g.split(':')[1].split('|')
 s=set(w.split())
 c=len(s&(set(m.split())))
 x,i=n[i],i+1
 for j in range(c):
   n[i+j]+=x
print(sum(n))
