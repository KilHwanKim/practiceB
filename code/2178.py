def findM(route):
  w= len(route[0])
  h = len(route)
  visited = [[0]*w for _ in range(h)]
  Q = [[0,0]]
  visited[0][0]=1
  while True:
    temp = Q.pop(0)
    x, y = temp[0],temp[1]
    if x == w-1 and y ==h-1:
      return visited[h-1][w-1]
    if x< w-1 and route[y][x+1] ==1 and visited[y][x+1] ==0:
      Q.append([x+1,y])
      visited[y][x+1]+=visited[y][x]+1
    if y< h-1 and route[y+1][x] ==1 and visited[y+1][x] ==0:
      Q.append([x,y+1])
      visited[y+1][x]+=visited[y][x]+1
    if x >0 and route[y][x-1] ==1 and visited[y][x-1] ==0:
      Q.append([x-1,y])
      visited[y][x-1]+=visited[y][x]+1
    if y >0 and route[y-1][x] ==1 and visited[y-1][x] ==0:
      Q.append([x,y-1])
      visited[y-1][x]+=visited[y][x]+1
h, w = map(int,input().split())
route = []
for i in range(h):
  route.append(list(map(int,list(input()))))
print(findM(route))    
