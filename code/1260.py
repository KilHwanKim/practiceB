n,m,s =map(int,input().split())
link = dict()
for i in range(1,1+n):
    link[i]=[]
for _ in range(m):
    a,b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)
visited =[0]*(n+1)
def DFS(s):
    visited[s]=1
    print(s,end=" ")
    for i in sorted(link[s]):
        if visited[i]==0:
            DFS(i)
17
18
19
20
21
22
23
24
25
26
27
DFS(s)
visited =[0]*(n+1)
print()
BFS(s)
