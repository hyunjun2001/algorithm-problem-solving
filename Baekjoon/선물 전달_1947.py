# 백준 선물 전달 문제이다.
# 문제 번호는 1947번.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input().strip())
memo = [-1] * (N+1)
mod = 1_000_000_000

def search(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    if memo[num] != -1:
        return memo[num]

    memo[num] = (num-1) * (search(num-1) + search(num-2)) % mod
    return memo[num]


print(search(N))



n = int(input().strip())
mod = 1_000_000_000
d = [0] * 1000001
d[1] = 0
d[2] = 1

for i in range(3, n+1):
    d[i] = (i-1) * (d[i-2] + d[i-1]) % mod

print(d[n])
