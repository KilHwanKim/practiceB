def back(x):
    global c,n,number
    if x==6:
        print(" ".join([str(number[i]) for i in c]))
    else:
        for i in range(n):
            c[x]=i
            if x==0 or c[x-1] < c[x]:
                10
11
12
13
14
15
16
    n = in_list[0]
    number = in_list[1::]
    back(0)
    print()
    22
