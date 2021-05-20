def find123(n):
  C = 0
  Q = [[0]]
  while Q:
    temp = Q.pop(0)
    templist = []
    for i in temp:
      if i==n:
        C+=1
      elif i<n:
        templist.append(i+1)
        templist.append(i+2)
        templist.append(i+3)
    if templist:    
      Q.append(templist)
  return C 
n = int(input())
for x in range(n):
  print(find123(int(input())))
