import sys
def power(a,b):
    if b==0:
        return 1
    if b % 2==1:
        return (power(a,b//2) ** 2 *a) % p
    else:
        return (power(a,b//2) ** 2) % p
n, k = map(int,sys.stdin.readline().split())
p = 1000000007
fac = [1,1]
for i in range(2,n+1):
    fac.append((fac[-1]*i)%p)
a = fac[-1]
b = (fac[n-k] * fac[k])%p
print(((a%p) * (power(b, p-2))%p)%p)
18
