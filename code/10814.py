import sys
n = int(input())
result = []
for _ in range(n):
    word = sys.stdin.readline().split()
    word[0]  = int(word[0]) 
    result.append(word)
result.sort(key = lambda x: (x[0]))
for age,name in result:
    print(age,name)
