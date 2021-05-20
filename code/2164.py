from collections import deque
n = int(input())
d = deque()
for i in range(n):
    d.append(i+1)
while True:
    if len(d)==1:
        print(d.popleft())
        break
    d.popleft()
    d.append(d.popleft())
print()
## 리스트쓰면 시간 초가
