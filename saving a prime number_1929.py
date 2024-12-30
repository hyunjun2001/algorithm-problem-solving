# 백준 소수 구하기 문제이다.
# 문제 번호는 1929번

import math
import sys

input = sys.stdin.readline

start, end = map(int, input().split())
arr = [0] * (end + 1)

for i in range(2, end + 1):
    arr[i] = i

for i in range(2, int(math.sqrt(end)) + 1):  # 제곱근까지만 연산 수행
    if arr[i] == 0:
        continue
    for j in range(i + i, end + 1, i):
        arr[j] = 0

for i in range(start, end + 1):
    if arr[i] != 0:
        print(arr[i])
