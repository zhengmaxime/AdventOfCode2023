l = open('f').readlines()
digits_to_find = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dic = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
s = 0
for e in l:
  min_index = float('inf')
  min_d = ''
  max_index = -1
  max_d = ''
  for d in digits_to_find:
    ind = e.find(d)
    rind = e.rfind(d)
    if ind != -1 and ind < min_index:
      min_index = ind
      min_d = d
    if rind != -1 and rind > max_index:
      max_index = rind
      max_d = d
  nb = ''
  if min_d in dic.keys():
    nb += dic[min_d]
  else:
    nb += min_d
  if max_d in dic.keys():
    nb += dic[max_d]
  else:
    nb += max_d
  s += int(nb)
print(s)