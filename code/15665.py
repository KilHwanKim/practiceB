def back (x):
    if x == m:
        ans.append([number_list[x] for x in check_list])
    else:
        for i in range(n):
            check_list[x] = i
            back(x+1)
9
11
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
