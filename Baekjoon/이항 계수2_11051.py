# 백준 이항 계수 2 문제이다.
# 문제 번호는 11051번

import sys
input = sys.stdin.readline

n, k = map(int, input().split())


def factorial(num):
    temp = 1
    for i in range(1, num+1):
        temp *= i
    return temp


ans = factorial(n) // (factorial(k) * factorial(n-k))
ans = ans % 10007

print(ans)