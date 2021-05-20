def isValid(String):
    c = 0
    for val in list(String):
        if val == "(":
            c+=1
        else:
            c-=1
        if c<0:
            return "NO"
    if c==0:
        return "YES"
    else:
        return "NO"
n = int(input())
for _ in range(n):
    print(isValid(input()))
