A = input().split("-")
s = sum(list(map(int,A[0].split("+"))))
for val in A[1:]:
    s-=sum(list(map(int,val.split("+"))))
print(s)
