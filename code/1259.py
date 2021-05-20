def isPel(n):
    word = str(n)
    s = 0
    e = len(word)-1
    while s <=e:
        if word[s] != word[e]:
            return "no"
        s+=1
        e-=1
    return "yes"
12
13
14
15
16
17
18
