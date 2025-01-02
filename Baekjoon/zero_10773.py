# 백준 제로 문제이다.
# 문제 번호는 10773번

import sys
input = sys.stdin.readline

stack = []

n = int(input())

ans = 0

for i in range(n):
    num = int(input())
    if num == 0:
        if stack:
            stack.pop()
        else:
            continue
    else:
        stack.append(num)

for i in stack:
    ans += i

print(ans)
