import sys
from collections import deque
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]
while True:
    ans = 0
    w,h = map(int,sys.stdin.readline().split())
    if w ==0 and h ==0:
        break
    ground = []
    visited= [ ]
    for j in range(h):
        ground.append(list(map(int,sys.stdin.readline().split())))
        visited.append([0]*w)
    for j in range(h):
        for i in range(w):
            if ground[j][i] ==1 and visited[j][i]==0:
                q = deque()
                ans +=1
                q.append([j,i])
                visited[j][i]=1
                while q:
                    y,x = q.popleft()
25
26
27
28
29
30
31
    print(ans)
34
