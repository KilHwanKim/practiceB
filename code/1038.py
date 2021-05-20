def back(x):
    global m ,n_list,answer
    if x==m:
        answer.append(int("".join(map(str,n_list))))
    else:
        for i in range(10):
            n_list[x] = i
            if x==0 or n_list[x-1]> n_list[x]:
                back(x+1)
answer = []
for m in range(1,11):
    n_list = [0]*m
    back(0)
n = int(input())
if len(answer)<=n:
    print(-1)
else:
    print(answer[n])
