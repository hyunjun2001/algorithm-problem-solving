# 백준 카드 정렬하기 문제이다.
# 문제 번호는 1715번

import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
cards = []
for i in range(n):
    heapq.heappush(cards, int(input().strip()))

total = 0


while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    sum_value = a+b

    total += sum_value
    heapq.heappush(cards, sum_value)

print(total)
