n = int(input())
A = list(map(int,input().split()))
A.sort()
B = [sum(A[:a+1]) for a in range(n)]
print(sum(B))
