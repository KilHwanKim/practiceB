## ���
def gcd(a,b):
  result =1 
  ab = a*b
  while result!=0:
    result = a%b
    a =b 
    b = result
  return int(ab/a)
number = int(input())## ���� ��
12
13
14
15
