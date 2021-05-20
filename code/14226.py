from _collections import deque
n = int(input())
screen = 1
board = 0
cnt = 0
q = deque()
8
9
10
while q:
    s,b,c = q.popleft()
14
15
        print(c)
        break
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
            q.append([s-1,b,c+1])## 하나 삭제
            visited[s-1][b]=1
