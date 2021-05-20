import sys
3
class MinHeap:
6
7
8
    def insert(self, number):
        self.data.append(number)
        l = len(self.data) - 1
        while l > 1:
            if self.data[l] < self.data[(l // 2)]:
                self.data[l], self.data[l // 2] = self.data[l // 2], .data[l]
                l = l // 2
            else:
                break
19
20
21
22
23
24
25
26
27
    def minHeapify(self, i):
        left = i * 2
        right = (i * 2) + 1
        smallest = i
        if left < len(self.data) and self.data[i] > self.data[left]:
            smallest = left
35
36
37
38
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], .data[i]
            self.minHeapify(smallest)
43
n = int(input())
H = MinHeap()
for _ in range(n):
    val = int(sys.stdin.readline())
    if val == 0:
        print(H.remove())
    else:
        H.insert(val)
53
55
