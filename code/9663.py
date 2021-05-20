n = int(input())
number_list = [0]*(n)
c = 0
def back(x):
    global n,c,number_list
    if x==n:
        c+=1
    else:
        for i in range(n):
            number_list[x]=i
            if check(x):
                back(x+1)
def check(x):
    for i in range(x):
        if ( number_list[x] == number_list[i]) or  (abs(number_list[x][i])==x-i):
            return False
    return True
back(0)
print(c)
