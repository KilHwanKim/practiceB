def check(x, y, n):
    global c_list, paper
    select = paper[y][x]
    for xx in range(n):
        for yy in range(n):
            if paper[y + yy][x + xx] != select:
                m = n // 3
                for mi in range(3):
                    for mj in range(3):
                        check(x + m * mi, y + m * mj, m)
                return
13
14
16
17
18
19
20
21
22
23
24
