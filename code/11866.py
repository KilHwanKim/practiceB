n,k = map(int,input().split())
L = list(range(1,n+1))
ind = k-1
answer="<"
while len(L)>1:
    answer+=str(L.pop(ind)) +", "
    ind =(ind+k-1)%len(L)
answer+=str(L.pop())+">"
print(answer)
