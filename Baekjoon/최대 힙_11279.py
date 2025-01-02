# 백준 최대 힙 문제이다.
# 문제 번호는 11279번

import sys
import heapq
input = sys.stdin.readline

n = int(input().strip())
arr = []

for i in range(n):
    temp = int(input().strip())
    if temp == 0:
        if arr:
            print(-heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, -temp)

