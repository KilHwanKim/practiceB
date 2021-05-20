s , b  = map(int ,input().split())
Q = [[s,0]]
visited = [0]*100001
visited[s]=1
while Q :
  val  =  Q.pop(0)
  temp = val[0]
  c = val[1]
  if temp== b:
    print(c) 
    break
13
14
15
16
17
  x = temp +1 
  if 0<=x<=100000 and visited[x]==0:
    Q.append([x,c+1])
    visited[x]=1
23
24
25
26
