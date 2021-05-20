n = int(input())
time_list = []
for _ in range(n):
  time_list.append(list(map(int,input().split())))
time_list.sort(key = lambda x: (x[1],x[0]) )
answer= 0 
end = 0
for s,e in time_list:
  if s >= end:
    end = e
    answer+=1
print(answer)
