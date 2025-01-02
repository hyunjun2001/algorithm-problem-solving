# 백준 스택 문제이다.
# 문제 번호는 10828번

import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    order = input().split()
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order[0] == 'size':
        print(len(stack))
    elif order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
