import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())
p_list = list(range(n+1))
def findP(number):
    global p_list
    if p_list[number] == number:
        return number
    else:
        p_list[number] = findP(p_list[number])
        return findP(p_list[number])
for ind in range(m):
    val = list(map(int,sys.stdin.readline().split()))
    if val[0]==1:
        if findP(val[1]) == findP(val[2]):
            print("YES")
        else:
            print("NO")
20
21
22
23
24
25
27
