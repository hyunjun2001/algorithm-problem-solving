# 백준 1,2,3 더하기 문제이다.
# 문제 번호는 9095번

import sys
input = sys.stdin.readline

t = int(input().strip())

arr = [int(input().strip()) for _ in range(t)]

d = [0] * 12

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, max(arr)+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for i in arr:
    print(d[i])