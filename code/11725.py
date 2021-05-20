import sys
sys.setrecursionlimit(10**7) 
input = sys.stdin.readline
n = int(input())
root = [[]for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    root[a].append(b)
    root[b].append(a)
visited = [0]*(n+1)
p = [0]*(n+1)
def find(parent):
    global visited,p
    for i in root[parent]:
        if visited[i]==0:
            visited[i] = 1
            find(i)
19
20
find(1)
for i in p[2::]:
    print(i)
25
