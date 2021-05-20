N = int(input())
for _ in range(N):
    h,w,n = map(int,input().split())
    print("{}{:0>2}".format(h if n%h==0 else n%h,(n-1)//h+1)) 
    6
