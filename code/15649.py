def dfs(n,s):
  result = []
  stack = []
  for i in range(1,n+1):
    stack = [[i]]
    while stack: 
      temp = stack.pop()
      if len(temp) ==s:
        result.append(temp)
      else:
        for i in range(n,0,-1):
          if i not in temp:
            stack.append(temp+[i])
  return result
n ,s = map(int,input().split())
for x in dfs(n,s):
  print(' '.join(map(str,x)))
