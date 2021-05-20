link_list = []
l = int(input())
n = int(input())
for _ in range(n):
    link_list.append(list(map(int,input().split())))
visited = [0]*l
Q = [1]
visited[0] =1 
while Q:
    temp = Q.pop(0)
    for ind,val in  enumerate(link_list):
        if temp in val:
            A = val.copy()
            A.remove(temp)
            16
17
18
19
20
            22
            24
