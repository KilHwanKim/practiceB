def back (x):
    if x == m:
        ans.append([number_list[x] for x in check_list])
    else:
        for i in range(n):
            check_list[x] = i
            if x==0 or check_list[x-1]<= check_list[x]:
                back(x+1)
10
12
13
14
15
16
17
18
19
20
21
22
