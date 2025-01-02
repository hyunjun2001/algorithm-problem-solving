# 백준 Four Squares 문제이다.
# 문제 번호는 17626번

import sys
import math
input = sys.stdin.readline

n = int(input().strip())
dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    temp = 10000
    
    for j in range(1, int(math.sqrt(i))+1):
        temp = min(temp, dp[i - (j ** 2)])
    dp[i] = temp + 1

print(dp[n])
