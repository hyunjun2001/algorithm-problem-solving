# 백준 2xn 타일링2 문제이다.
# 문제 번호는 11727번이다.

import sys
input = sys.stdin.readline

n = int(input().strip())
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 10007

print(d[n])
