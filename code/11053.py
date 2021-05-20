n = int(input())
number_list = list(map(int,input().split()))
count_list = [1]*n
for i in range(n):
    ind = i
    m = [0] 
    while i > 0 :
        i-=1
        if number_list[i]< number_list[ind]:
            m.append(count_list[i])
12
13
