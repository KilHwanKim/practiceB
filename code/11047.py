n, target = map(int,input().split())
coin = [int(input()) for _ in range(n)]
coin.sort(reverse=True)
c=0
for val in coin:
    if val <= target:
        c+=target//val
        target -= (target//val)*val
print(c)
