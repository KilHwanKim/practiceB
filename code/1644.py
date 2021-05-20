end =  int(input())
prime_l = []
def prime(start,end):
    global prime_l
    result = list (range( end+1))
    for val in result[:end//2+1]:
        if val != 0 and val != 1:
            for change in result[val*val::val]:
                result[change]=0
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
22
23
24
25
26
27
28
print(answer)
