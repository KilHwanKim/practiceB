n , target = map(int,input().split())
c = 1
while n!=target:
    if len(str(target))>1 and str(target)[-1] == "1":
        target=int(str(target)[:-1])
        c+=1
    elif target%2==0:
        target = target//2
        c+=1
    else:
        c=-1
        break
print(c)
