n = int(input())
number_list = list(map(int,input().split()))
del_number = int(input())
child = [[] for i in range(n)]
root = []
for ind,val in enumerate(number_list):
    if val == -1:
        root.append(ind)
    elif ind!= del_number:
        child[val].append(ind)
answer = 0
def dfs(x,del_number):
    global child ,answer
    if x == del_number:
        return
    if child[x] :
        for i in child[x]:
            dfs(i,del_number)
    else:
        answer+=1
for i in root:
    dfs(i,del_number)
print(answer)
