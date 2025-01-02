# 백준 계단 오르기 문제이다.
# 문제 번호는 2579번

import sys
input = sys.stdin.readline

n = int(input().strip())
stairs = [0] * 301

for i in range(1, n+1):
    temp = int(input().strip())
    stairs[i] = temp

dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(dp[1] + stairs[3], stairs[2]+stairs[3])


for i in range(4, n+1):
    dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])


print(dp[n])
