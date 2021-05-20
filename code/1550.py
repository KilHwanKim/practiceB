word = input()
result = 0
for ind,val in enumerate(list(word)[::-1]):
  result+=int(val,16)*(16**ind)
print(result)
