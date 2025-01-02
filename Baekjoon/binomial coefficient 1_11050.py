# 백준 이항 계수 1 문제이다.
# 문제 번호는 11050번

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = 1  # 분자에 들어갈 n!
b = 1  # 분모에 들어갈 (n-k)!
c = 1  # 분모에 들어갈 k!

for i in range(1, n+1):
    a *= i

for i in range(1, n-k+1):
    b *= i

for i in range(1, k+1):
    c *= i

print(int(a / (b * c)))
