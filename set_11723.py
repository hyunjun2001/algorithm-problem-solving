# 백준 집합 문제이다.
# 문제 번호는 11723번

import sys
input = sys.stdin.readline

n = int(input())

S = set()

for _ in range(n):
    order = list(input().split())
    if order[0] == 'add':
        S.add(int(order[1]))
    if order[0] == 'remove':
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            continue
    if order[0] == 'check':
        if int(order[1]) in S:
            print(1)
        else:
            print(0)
    if order[0] == 'toggle':
        if int(order[1]) in S:
            S.remove(int(order[1]))
        else:
            S.add(int(order[1]))
    if order[0] == 'all':
        S = set([i for i in range(1, 21, 1)])
    if order[0] == 'empty':
        S = set()
