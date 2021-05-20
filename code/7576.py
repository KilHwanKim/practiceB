w, h = map(int,input().split())
tomato = []
for _ in range(h):
  tomato.append((list(map(int,input().split()))))
dx = [1,-1,0,0]
dy = [0,0,-1,1]
C= -1
Q = []
visited = [[0]*w for i in range(h)]
for x in range(w):
    for y in range(h):
        if tomato[y][x] ==1:      
            Q.append([x,y])
15
16
17
18
19
20
        if visited[y][x]==0:
            for ind in range(4):
                nx = x+ dx[ind] 
                ny = y + dy[ind]
                if nx<w and ny < h and nx>=0 and ny >= 0 and visited[][]==0 and tomato[ny][nx] == 0:
                    tomato[ny][nx] =1
                    temp_list.append([nx,ny])
        visited[y][x] =1
    Q = temp_list
    C+=1
for ind,x in enumerate(tomato):
    if 0 in x:
        print(-1)
        break
    if ind == len(tomato)-1:
        print(C)
38
