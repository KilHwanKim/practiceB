n = int(input())
answer=0
def isPrime(number):
    if number==2:
        return 1
    if number ==1:
        return 0
    for i in range(2,number):
        if number%i==0:
            return 0
    return 1
number_list = list(map(int,input().split())) 
for num in number_list:
    answer+=isPrime(num)
print(answer)
