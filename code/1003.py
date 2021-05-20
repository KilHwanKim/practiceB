answer = [[1,0],[0,1]]
while True:
    if len(answer)>40:
        break
    else:
        x = answer[-1][0] +answer[-2][0]
        y = answer[-1][1] +answer[-2][1]
        answer.append([x,y])
n = int(input())
for _ in range(n):
    print(" ".join(map(str,answer[int(input())])))
