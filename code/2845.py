w, h = map(int,input().split())
article = map(int,input().split())
result = ""
for val in article:
  result+=" "+str(val-w*h)
print(result.strip())
