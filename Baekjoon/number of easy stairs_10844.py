# 백준 쉬운 계단 수 문제이다.
# 문제 번호는 10844번
# 점화식 설정에 있어 2차원 d 배열을 만들어 값을 기억해야 했다.

import sys
input = sys.stdin.readline

n = int(input().strip())
d = [[0] * 10 for _ in range(n+1)]

for i in range(1, 10):
    d[1][i] = 1

MOD = 1000000000

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i-1][1]
        elif j == 9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]

print(sum(d[n]) % MOD)
