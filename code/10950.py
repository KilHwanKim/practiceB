N=int(input())
numlist=[]
for i in range(N):
    a,b = input().split()
    numlist.append([int(a),int(b)])
for j in numlist:
    print(j[0]+j[1])
