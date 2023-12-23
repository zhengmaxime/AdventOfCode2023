from math import sqrt
t,l=[int(''.join(open('f').readlines()[i].split(':')[1].split()))for i in[0,1]]
d=sqrt(t*t-4*l)
print(int(-.5*(-t-d)+.5*(-t+d)))

# 0.5(-t-d) + 0.5(-t+d) <=> 0.5(t+d-t+d) <=> d
