import sys
n,x = map(int,sys.stdin.readline().split())
matrix = [[int(x)%1000 for x in sys.stdin.readline().split()] for _ in (n)]
5
6
7
8
9
10
11
12
13
def squre(matrix,x):
    if x==1:
        return matrix
    else:
        temp = squre(matrix,x//2)
        if x%2 == 0:
            return multi(temp,temp)
        else:
            return multi(multi(temp,temp),matrix)
for val in squre(matrix,x):
    print(" ".join([str(i) for i in val]))
