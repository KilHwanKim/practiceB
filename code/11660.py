import sys
n, m = map(int, input().split())
matrix = [[0]*(n+1)]
matrix += [[0]+list(map(int, sys.stdin.readline().split())) for _ in (n)]
6
7
8
9
10
11
12
13
14
15
