import sys
class MaxHeap():
4
5
6
    def insert(self,number):
        self.data.append(number)
        i = len(self.data) -1
        while i > 1:
            if self.data[i] > self.data[i//2]:
                self.data[i] , self.data[i//2] = self.data[i//2] , self.[i]
                i = i//2
            else: break
    16
17
18
19
20
21
22
23
24
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
        return
41
42
43
44
45
46
47
48
