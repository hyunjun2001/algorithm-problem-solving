# 백준 팩토리얼 0의 개수 문제이다.
# 문제 번호는 1676번

from math import factorial
import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for x in str(factorial(n))[::-1]:
    if x != '0':
        break
    ans += 1

print(ans)
