n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int,input().split())))    
w ,b = 0,0
7
8
9
10
11
12
13
14
15
16
            if test[y][x] !=color:
                l = L//2
                d1 = [x[:l] for x in test[:l]]
                d2 = [x[l:] for x in test[:l]]    
                d3 = [x[:l] for x in test[l:]]
                d4 = [x[l:] for x in test[l:]]
                divide(d1)
                divide(d2)
                divide(d3)
                divide(d4)
                check = False
                break
    if check:
        if color :
            b+=1
        else :
            w+=1
divide(paper)
print(w)
print(b)
