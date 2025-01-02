# 백준 최소 힙 문제이다.
# 문제 번호는 1927번

import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input().strip())

for i in range(n):
    temp = int(input().strip())
    if temp == 0:
        if heap:
            num = heapq.heappop(heap)
            print(num)
        else:
            print(0)
    else:
        heapq.heappush(heap, temp)
