# 2503, ���� �߱�
import sys
from itertools import permutations
5
6
num = list(permutations(n, 3))  # ������ 3���� ����
9
10
11
12
13
14
    # num : 3�� ����Ʈ
    leng = len(num)
    for i in range(leng):
        s_cnt = b_cnt = 0   # ��Ʈ ����, �� ���� 0 �ʱ�ȭ
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
            num.remove(num[i])      # ��Ʈ ����, �� ���� �ٸ��� �迭���� ����
            removed_cnt += 1
33
