def back(x):
    global m,n,number_list,check_list
    if x==m:
        print(" ".join([str(i) for i in check_list]))
    else:
        for i in number_list:
            check_list[x]=i
            if x==0 or check_list[x-1]<= check_list[x]:
                back(x+1)
             11
12
13
14
15
