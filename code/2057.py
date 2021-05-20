##팩토리얼 분해
from itertools import combinations
answer =[]
def fac(n):
  if n==1 or n==0:
    return 1
  else:
    return n*fac(n-1)
N = int(input())## 입력 받은 수
i = 0
if N==0:
  print("NO")
else:
  while True :
    if fac(i)>N:
      break
    else :
      answer.append(fac(i))
      i+=1
  L = len(answer)
  for i in range(1,L+1):
    S = [sum(x) for x in list(combinations(answer,i)) ]
    if N in S:
      print("YES")
      break
    if i==L:
      print("NO")
