from collections import deque
import sys
4
5
6
7
8
9
10
11
12
        temp = q.popleft()
        n = temp[0]
        code = temp[1]
        if int(n) == target:
            print(code)
            break
20
21
22
23
24
        S = str((int(n) - 1) % 10000).zfill(4)
        if visited[int(S)] == 0:
            q.append([S, code + "S"])
            visited[int(S)] = 1
        n4 = str(n).zfill(4)
31
32
33
34
35
        R = (str(n4)[-1] + str(n4)[0:-1])
        if visited[(int(R))] == 0:
            q.append([R, code + "R"])
            visited[int(R)] = 1
41
