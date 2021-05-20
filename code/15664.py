def back(x):
    global n, m, check_list, number_list, visited, ans
    if x == m:
        ans.append([number_list[x] for x in check_list])
    else:
        for i in range(n):
8
9
                check_list[x] = i
                if x == 0 or check_list[x - 1] <= check_list[x]:
                    visited[i] = 1
                    back(x + 1)
                    visited[i] = 0
16
17
18
19
20
21
22
23
24
25
26
