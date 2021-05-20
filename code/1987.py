from collections import deque
import sys
sys.setrecursionlimit(10**5)
R, C = map(int, sys.stdin.readline().split())
6
7
8
9
q = deque()
q.append((0, 0,1, abc[0][0]))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0
while q:
    x, y, cnt,word = q.pop()
    answer = max(cnt , answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < C and nx >= 0 and ny < R and ny >= 0:
            if abc[ny][nx] not in word:
                q.append((nx, ny,cnt+1, word + abc[ny][nx]))
25
26
28
