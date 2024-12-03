# 백준 수 정렬하기 문제이다.
# 문제 번호는 2750번

import sys
input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr:
    print(i)