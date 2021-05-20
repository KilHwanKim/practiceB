import sys
n = int(sys.stdin.readline())
number_list = [0]*10001
for i in range(n):
    number_list[int(sys.stdin.readline())]+=1
for ind,val in enumerate(number_list):
    if val !=0:
        for i in range(val):
            print(ind)
