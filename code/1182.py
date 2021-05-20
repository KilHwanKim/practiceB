## 부분 수열의 합 
from itertools import combinations
n ,s = map(int,input().split())
answer=0
number_list = list(map(int,input().split()))
for c in range(1,n+1):
  for i in list(combinations(number_list,c)):
    if sum(i) == s:
      answer+=1
print(answer)
