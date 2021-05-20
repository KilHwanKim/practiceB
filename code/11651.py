import sys
n = int(sys.stdin.readline())
number_list = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    number_list.append([a,b])
number_list.sort(key= lambda x : (x[1],x[0]))
for x,y in number_list:
    print(x,y)
