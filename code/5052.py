import sys
n = int(sys.stdin.readline())
def check():
    for i in range(ca-1):
        if number_list[i] == number_list[i+1][0:len(number_list[i])]:
            print("NO")
            return
    return print("YES")
10
11
12
13
14
15
16
17
