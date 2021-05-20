wordlist =  map(int,input().split())
result = 0
for i in wordlist:
  result+=i**2
print(result%10)
