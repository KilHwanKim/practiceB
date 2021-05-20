def G(a,b):
  result =1 
  ab = a*b
  while result!=0:
    result = a%b
    a =b 
    b = result
  print(a)
  print(int(ab/a))
a,b = map(int,input().split())
G(a,b)
