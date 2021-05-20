def binary(n):
    global only_one
    s= 0
    e = len(only_one)-1
    m = (s+e)//2
    while  only_one[m]!=n:
        if only_one[m]<n:
            s=m+1
            m = (s+e)//2
        else:
            e = m
            m = (s+e)//2
    return m
n = int(input())
number_list = list(map(int,input().split()))
only_one = sorted(list(set(number_list)))
answer = [str(binary(x)) for x in number_list]
print(" ".join(answer))
20
