n , m = map(int,input().split())
fact = [1,1]
p = 1000000007
for i in range(2,n+1):
    fact.append((fact[-1]*i)%p)
def power(a,b):
    if b==0:
        return 1
    if b %2==0:
        return (power(a,b//2)**2)%p
    else:
        return ((power(a,b//2)**2)*a)%p
x = fact[n]
y = (fact[m] * fact[n-m])%p
print((x%p)*(power(y,p-2)%p)%p)
