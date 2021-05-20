from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
RGB = []
for _ in range(n):
    RGB.append(list(map(int,input().split())))
for ind in range(1,n):
    RGB[ind][0]  = min([RGB[ind-1][1],RGB[ind-1][2]])+RGB[ind][0]
    RGB[ind][1] = min([RGB[ind-1][0],RGB[ind-1][2]])+RGB[ind][1]
    RGB[ind][2] = min([RGB[ind-1][0],RGB[ind-1][1]])+RGB[ind][2]
print(min(RGB[-1]))
