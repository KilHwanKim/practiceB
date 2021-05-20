## 수 정렬하기2
N = int(input())
answer = []
for i in range(N):
  answer.append(int(input()))
answer.sort()
for x in answer:
  print(x)
