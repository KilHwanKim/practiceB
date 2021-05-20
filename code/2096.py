n = int(input())
number =[list(map(int,input().split())) for _ in range(n)]
big = number[0]
small = number[0]
for i in range(1,n):
    big  = [max ( big[0],big[1])+ number[i][0] , \
           max ( big[0],big[1],big[2])+ number[i][1], \
           max ( big[1],big[2])+ number[i][2]]
    small = [min(small[0], small[1]) + number[i][0], \
            min(small[0], small[1], small[2]) + number[i][1], \
            min(small[1],small[2]) + number[i][2]]
print(max(big),min(small))
