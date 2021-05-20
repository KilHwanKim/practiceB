import heapq
import sys
4
class binaryQ():
7
8
9
10
11
    def insert(self, number):
        number = int(number)
        heapq.heappush(self.minH, number)
        heapq.heappush(self.maxH, -1 * number)
        if number in self.visited:
            self.visited[number] += 1
        else:
            self.visited[number] = 1
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
    def getmaxmin(self):
        minVal, maxVal = "", ""
        while self.minH:
            number = heapq.heappop(self.minH)
            if number in self.visited:
                minVal = number
                break
        while self.maxH:
            number = heapq.heappop(self.maxH)
            number = -1 * number
            if number in self.visited:
                maxVal = number
                break
        return maxVal, minVal
56
input = sys.stdin.readline
c = int(input())
for _ in range(c):
    n = input()
    n = int(n)
    bq = binaryQ()
    for __ in range(n):
        word = input().split()
        if word[0] == "I":
            bq.insert(word[1])
        elif word[0] == "D":
            bq.remove(int(word[1]))
    result = bq.getmaxmin()
    if result[0] == "":
        print("EMPTY")
    else:
        print(result[0], result[1])
