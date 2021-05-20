import sys
from itertools import combinations
number_list = []
for _ in range(9):
    number_list.append(int(sys.stdin.readline()))
number_list.sort()
for i in list(combinations(number_list,7)):
    if sum(i)==100:
        for val in i:
            print(val)
        break
13
