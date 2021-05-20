s = 0
def Z(n,y,x):
    global s
    if n==1:
        if x==0 and y==0:
            return s
        elif x==1 and y==0:
            return s+1
        elif x==0 and y==1:
            return s+2
        else:
            return s+3
    else:
        mid = 2**(n-1)
        if x< mid and y < mid: ## 1사분면
            return Z(n-1,y,x)
        elif x>=mid and  y < mid: ## 2사분면
            s+=mid*mid
            return Z(n-1,y,x-2**(n-1))
        elif x< mid and  y>=mid:## 3사분면
            s+=mid*mid*2
            return Z(n-1,y-mid,x)
        else :## 4사분면
            s+=mid*mid*3
            return Z(n-1,y-mid,x-mid)
n,y,x = map(int,input().split())
print(Z(n,y,x))
