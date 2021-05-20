import sys
from collections import deque
position ,target = map(int,sys.stdin.readline().split())
q = deque()
cnt = 0
visited = [-1 for i in range(200001)]
q.append([position,cnt])
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
21
22
23
24
    26
