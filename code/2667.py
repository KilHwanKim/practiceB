n = int(input())
visited = [[0]*n for x in range(n)]
c_list = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
route =[]
for _ in range(n):
    route.append(list(map(int,list(input()))))
for x in range(n):
    for y in range(n):
        if route[y][x]==1 and visited[y][x]==0:
            stack = []
            stack.append([x,y])
            visited[y][x]=1
            c_list.append(1)
            while stack:
                temp = stack.pop()
                tx = temp[0]
                ty = temp[1]
21
22
23
24
25
26
27
28
29
30
31
