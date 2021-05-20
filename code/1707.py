import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    v,e = map(int,sys.stdin.readline().split())
    link = [[] for i in range(v+1)]
    for __ in range(e):
        a,b = map(int,sys.stdin.readline().split())
        link[b].append(a)
        link[a].append(b)
    ans = "YES"
    visited = [0]*(v+1)
    for i in range(1,v+1):
        if visited[i]==0:
            q = deque()
            visited[i]=1
            q.append(i)
19
20
21
22
23
24
25
26
27
28
29
31
32
34
