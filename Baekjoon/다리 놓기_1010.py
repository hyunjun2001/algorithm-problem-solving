# 백준 다리 놓기 문제이다.
# 문제 번호는 1010번

# 순수 DP로만 접근하니 시간초과

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dp(n, m):
    if n == m:
        return 1
    if n == 1:
        return m
    if n <= m and n != 1:
        return dp(n, m-1) + dp(n-1, m-1)


T = int(input().strip())

for _ in range(T):
    N, M = map(int, input().split())
    print(dp(N,M))



# 이번엔 조합 공식으로 접근

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input().strip())

graph = [[0 for _ in range(30)] for _ in range(30)]


def factorial(n):
    temp = 1
    for i in range(1, n+1):
        temp *= i
    return temp


for _ in range(T):
    N, M = map(int, input().split())
    ans = factorial(M) // (factorial(M-N) * factorial(N))
    print(ans)
