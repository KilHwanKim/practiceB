n_list = [1, 1, 1, 2, 2]
for i in range(5,100+1):
    n_list.append(n_list[i-5]+n_list[i-1])
n = int(input())
for _ in range(n):
    print(n_list[int(input())-1])
