def back(x):
    global n,m,number_list
    if x==m:
        print(" ".join([str(i) for i in number_list]))
    else:
        for i in range(1,n+1):
            number_list[x]=i
            back(x+1)
n,m = map(int,input().split())
number_list = [0]*m
back(0)
