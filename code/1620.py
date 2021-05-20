import sys
input = sys.stdin.readline
N , M = map(int,input().split())
dic = {}
name_list =[]
for x in range(N):
  word = input().strip()
  dic[word] = x+1
  name_list.append(word)
for _ in range(M):
  val = input().strip()
  if val.isdigit():
    print(name_list[int(val)-1])
  else:
   print(dic[val])
