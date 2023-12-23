l = open('f').readlines()
s = 0
for e in l:
  nb = ''
  for c in e:
    if c.isdigit():
      nb += c
      break
  for c in e[::-1]:
    if c.isdigit():
      nb += c
      break
  s += int(nb)
print(s)