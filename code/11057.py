def c(n,m): ## 조합식
    answer = 1
    for i in range(n,n-m,-1):
        answer *=i
    for x in range(1,m+1):
        answer //=x
    return answer
n = int(input())
### 조합과 중봅조합으로 풀었습니다.
answer = 0
for i in range(1,n+1):
    answer+=(c(10,i)) *(c(n-1,n-i)) ## iH(n-i)값
    answer%=10007
print(answer)
