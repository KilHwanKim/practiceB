first = [1,1 ,2,2,2,8]
my_piece = map(int,input().split())
result = ""
for a, b in zip(first,my_piece):
  result+=" "+str(a-b)
print(result.strip())
