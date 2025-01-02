# 백준 파도반 수열 문제이다.
# 문제 번호는 9461번

import sys
input = sys.stdin.readline

t = int(input().strip())
dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1

def search(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = search(n-2) + search(n-3)
    return dp[n]

for i in range(t):
    n = int(input().strip())
    ans = search(n)
    print(ans)