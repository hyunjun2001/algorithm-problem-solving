# 백준 조약돌 꺼내기 문제이다.
# 문제 번호는 13251번

import sys
input = sys.stdin.readline

M = int(input().strip())
colors = list(map(int, input().split()))
K = int(input().strip())


def factorial(num):
    temp = 1
    for i in range(1,num+1):
        temp *= i
    return temp


total = factorial(sum(colors)) // (factorial(sum(colors)-K) * factorial(K))
part = 0

for color in colors:
    if color >= K:
        part += factorial(color) // (factorial(color-K) * factorial(K))


print(part / total)