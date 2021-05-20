import sys
n,m  = map(int,input().split())
number_list = list(map(int,sys.stdin.readline().split()))
sum_list = [0]*n
for i in range(n):
    if i==0:
        sum_list[i] = number_list[i]
    else:
        sum_list[i] =number_list[i]+ sum_list[i-1]
11
12
13
14
15
16
17
