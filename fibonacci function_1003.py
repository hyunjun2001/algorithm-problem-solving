# 피보나치 함수 문제이다.
# 문제 번호는 1003번.

import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    a, b = 1, 0
    for i in range(n):
        a, b = b, a+b
    print(a, b)