n = int(input())
RGB = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
nomal_c=0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for x in range(n):
    for y in range(n):
        if visited[y][x]==0:
            stack= []
            stack.append([x,y])
            visited[y][x]=1
            color = RGB[y][x]
            nomal_c+=1
            while stack:
                temp = stack.pop()
                tx = temp[0]
                ty = temp[1]
                for ind in range(4):
                    nx = tx+dx[ind]
                    ny = ty+dy[ind]
                    if nx<n and ny <n and nx>=0 and ny>=0 and visited[][nx] ==0 and  RGB[ny][nx] ==color:
                        stack.append([nx,ny])
                        visited[ny][nx]=1 
visited = [[0]*n for _ in range(n)]
cc=0
for x in range(n):
    for y in range(n):
        if visited[y][x]==0:
            stack= []
            stack.append([x,y])
            visited[y][x]=1
            color = RGB[y][x]
            if color =="G":
                color="R"
            cc+=1
            while stack:
                temp = stack.pop()
                tx = temp[0]
                ty = temp[1]
                for ind in range(4):
                    nx = tx+dx[ind]
                    ny = ty+dy[ind]
                    if nx<n and ny <n and nx>=0 and ny>=0 and visited[][nx] ==0 and  (RGB[ny][nx]=="G" and "R" or RGB[ny][nx] ) ==color:
                        stack.append([nx,ny])
                        visited[ny][nx]=1
print(nomal_c,cc)
