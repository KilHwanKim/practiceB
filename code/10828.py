import sys
n = int(input())
4
stack = []
for _ in range(n):
    word = sys.stdin.readline().split()
    if len(word)==2:
        stack.append(int(word[1]))
    else:    
        if word[0] == "size":
            print(len(stack))
        elif word[0] == "empty":
            if stack ==[]:
                print(1)
            else:
                print(0)
        else:
            if stack==[]:
                print(-1)
            elif word[0]=="pop":
                print(stack.pop())
            elif word[0]=="top":
                print(stack[-1])
