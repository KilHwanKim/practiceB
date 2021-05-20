import sys
from queue import Queue
n ,ca = map(int,sys.stdin.readline().split())
link_list = [[] for i in range(n+1)]
visited = [0]*(n+1)
for ind in range(ca):
    a,b = map(int,sys.stdin.readline().split())
    link_list[a].append(b)
    link_list[b].append(a)
c=0
for i in range(1,n+1):
    if visited[i]==0:
        q = Queue()
        c+=1
        q.put(i)
        while q.qsize()>0:
            temp = q.get()
            for x in link_list[temp]:
                if visited[x] ==0:
                    q.put(x)
                    visited[x] =1
print(c)
24
26
