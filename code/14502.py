import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
h , w = map(int,sys.stdin.readline().split())### h  세로 w가로
wall_list= []
for _ in range(h):
    wall_list.append(list(map(int,sys.stdin.readline().split())))
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
for item in list(combinations(zero,3)):
    n_wall_list = deepcopy(wall_list)
    for i,j in item:
        n_wall_list[j][i]=1
    q = deque()
    z = len(zero)-3
    for i,j in two:
        q.append([i,j])
31
    while q:
        x,y = q.popleft()
        for i in range(4):
36
37
38
39
40
41
42
43
