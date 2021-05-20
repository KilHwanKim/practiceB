dic = {}
all , find = map(int,input().split())
for i in range(all):
  K, V = map(str,input().split())
  dic[K] = V
for _ in range(find):
  print(dic[input()])
