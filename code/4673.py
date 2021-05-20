### ¼¿ÇÁ ³Ñ¹ö
answer = list(range(10001))
for i in range(1,10001):
  if answer[i] !=0:
    num = i
    while True:
      num = sum([int(j) for j in list(str(num))])+num
    9
10
11
12
13
14
