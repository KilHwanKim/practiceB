import sys
n , m = map(int,sys.stdin.readline().split())
link = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)
9
10
11
12
13
14
15
16
17
18
19
20
ans = 0
for i in range(n):
    dfs(i,0)
    visited[i] = 0
    if ans == 1:
        break
print(ans)
