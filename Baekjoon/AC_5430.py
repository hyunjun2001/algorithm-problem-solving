# 백준 AC 문제이다.
# 문제 번호는 5430번.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

for i in range(n):
    a = input().strip()
    m = int(input())
    flag = 1
    arr = input().strip()

    if m == 0:
        dq = deque()
    else:
        dq = deque(arr[1:-1].split(',')) 

    R = 0
    for i in range(len(a)):
        if a[i] == 'R':
            R += 1
        elif a[i] == 'D':
            if len(dq) == 0:
                print('error')
                flag = 0
                break
            else:
                if R % 2 == 0:
                    dq.popleft()
                else:
                    dq.pop()

    if flag == 0:
        continue
    else:
        if R % 2 == 0:
            print('[' + ",".join(dq) + ']')
        else:
            dq.reverse()
            print('[' + ",".join(dq) + ']')
