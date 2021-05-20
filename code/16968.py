### 백트랙킹으로 풀었습니다.
code = input()
abc = "abcdefghijklmnopqrstuvwxyz"
n = [0]*len(code)
c = 0
def back(x,code):
    global c,abc
    if x==len(code):
        c+=1
    else:
        if code[x]=="d":
            for i in range(10):
                n[x]=i
                if x==0 or n[x]!=n[x-1]:
                    back(x+1,code)
        else:
            for a in list(abc):
                n[x]=a
                if x==0 or n[x]!=n[x-1]:
                    back(x+1,code)
22
23
print(c)
