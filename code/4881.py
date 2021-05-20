### 4881 자리수의 
while True:
  a,b = map(int,input().split())
  if a==0 and b==0:
    break
  a_list= [a]
  b_list= [b]
  result =0
  while True:
    val_a = sum([int(i)**2 for i in list(str(a_list[-1]))])
    if val_a in a_list:
      break
    else:
      a_list.append(val_a)
  while True:
    val_b = sum([int(i)**2 for i in list(str(b_list[-1]))])
    if val_b in b_list:
      break
    else:
      b_list.append(val_b)
  for a_ind,a_x in enumerate(a_list):
    for b_ind,b_x in enumerate(b_list):
      if a_x == b_x:
        if result > a_ind + b_ind +2 or result ==0:
          result = a_ind + b_ind +2
      27
28
