import sys
k = int(sys.stdin.readline())
for _ in range(k):
    n = int(sys.stdin.readline())
    number_list= []
    for x in range(2):
        number_list.append(list(map(int,sys.stdin.readline().split())))
    number_list[0][1] += number_list[1][0]
    number_list[1][1] += number_list[0][0]
    for i in range(2,n):
        number_list[0][i] = number_list[0][i]+max(number_list[1][i-1],[1][i-2])
        number_list[1][i] = number_list[1][i] + max(number_list[0][i  ], number_list[0][i - 2])
    print(max(number_list[0][-1],number_list[1][-1]))
