# 백준 수 묶기 문제이다.
# 문제 번호는 1744번

import sys, heapq
input = sys.stdin.readline

n = int(input())
positive = []
negative = []

total = 0

for i in range(n):
    num = int(input().strip())
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()

for i in range(1, len(positive), 2):
    if positive[i-1] + positive[i] < positive[i-1] * positive[i]:
        total += (positive[i-1] * positive[i])
    else:
        total += (positive[i-1] + positive[i])

if len(positive) % 2 != 0:
    total += positive[-1]

for i in range(1, len(negative), 2):
    if negative[i-1] + negative[i] < negative[i-1] * negative[i]:
        total += (negative[i-1] * negative[i])
    else:
        total += (negative[i-1] + negative[i])

if len(negative) % 2 != 0:
    total += negative[-1]

print(total)
