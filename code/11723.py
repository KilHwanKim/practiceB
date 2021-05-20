import sys
n = int(input())
S = set()
for _ in range(n):
  temp = sys.stdin.readline().strip().split()
  if len(temp) ==1:
    if temp[0] == "all":
      S = set(range(1,21))
    else : 
      S = set()
  else:
    keyword ,val = temp[0], temp[1]
    val = int(val)
    if keyword == "add":
      S.add(val)
    elif keyword == "check":
      if val in S:
        print(1)
      else :
        print(0)
    elif keyword == "remove":
      S.discard(val)
    elif keyword == "toggle":
      if val in S:
        S.discard(val)
      else:
        S.add(val)
