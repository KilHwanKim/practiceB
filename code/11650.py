import sys
n  = int(input())
result = []
for _ in range(n):
    result.append(list(map(int,sys.stdin.readline().split())))
result.sort(key = lambda x: (x[0],x[1]))
for x,y in result:
    print(x,y)
