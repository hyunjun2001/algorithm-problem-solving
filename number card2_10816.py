# 백준 숫자카드 2 문제이다
# 문제 번호는 10816번

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())

numbers = {}
arr = list(map(int, input().split()))

m = int(input().strip())
arr_2 = list(map(int, input().split()))

for i in arr:
    if i not in numbers:
        numbers[i] = 1
    else:
        numbers[i] += 1

for i in arr_2:
    if i in numbers:
        print(numbers[i], end=' ')
    else:
        print(0, end=' ')
