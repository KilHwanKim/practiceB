def fac(n):
    if n==1 or n ==0:
        return 1
    else: 
        return n*fac(n-1)
n ,m = map(int,input().split())
print(fac(n)//(fac(m)* fac(n-m)))
