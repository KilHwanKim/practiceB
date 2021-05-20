# 2503, 숫자 야구
import sys
from itertools import permutations
5
6
num = list(permutations(n, 3))  # 순열로 3개씩 뽑음
9
10
11
12
13
14
    # num : 3개 리스트
    leng = len(num)
    for i in range(leng):
        s_cnt = b_cnt = 0   # 스트 개수, 볼 개수 0 초기화
        i -= removed_cnt
21
22
23
24
25
26
27
28
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])      # 스트 개수, 볼 개수 다르면 배열에서 제거
            removed_cnt += 1
33
