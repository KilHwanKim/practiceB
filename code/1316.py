# 그룹 단어 체커
N = int(input())
answer = N
for x in range(N):
  word = input()
  for ind in range(1,len(word)):
    if word[ind] != word[ind-1]:
      if word[ind-1] in word[ind::]:
        answer-=1
        break
print(answer)
    
