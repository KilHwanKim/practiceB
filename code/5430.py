from collections import deque
3
class AC:
    def __init__(self, number_list):
        self.d = deque()
        for val in number_list:
            self.d.append(int(val))
        self.sign = True
11
12
13
14
15
16
    def change(self):
        self.sign = not self.sign
20
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
        if self.sign:
            return list(self.d)
        else:
            return list(self.d)[::-1]
36
n = int(input())
for _ in range(n):
    code = input()
    m = int(input())
    number_list = input()
    if number_list == "[]":
        number_list = []
    else:
        number_list = list(map(int, number_list[1:-1].split(",")))
    ac = AC(number_list)
    print(str(ac.print_val(code)).replace(" ", ""))
