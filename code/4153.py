while True:
    a,b,c, = map(int,input().split())
    L = [a,b,c]
    L.sort()
    if a==0 and b==0 and c==0:
        break
    if L[-1]**2 ==L[0]**2 + L[1]**2:
        print("right")
    else:
        print("wrong")
    
