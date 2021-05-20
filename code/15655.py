def back(x):
    global n,m,check_list,number_list
    if x==m:
        print(" ".join([str(i) for i in check_list]))
    else:
        for i in number_list:
            check_list[x]=i
            if x==0 or check_list[x-1]< check_list[x]:
                back(x+1)
n,m = map(int,input().split())
number_list = list(map(int,input().split()))
number_list.sort()
check_list=[0]*m
back(0)
