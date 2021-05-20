def back(x):
    global n,m,number_list,ind_list
    if x==m:
        print(" ".join([str(number_list[i]) for i in ind_list]))
    else:
        for i in range(n):
            ind_list[x]=i
            if i not in ind_list[:x]:
                back(x+1)
n,m = map(int,input().split())
number_list = list(map(int,input().split()))
number_list.sort()
ind_list = [0]*m
back(0)
