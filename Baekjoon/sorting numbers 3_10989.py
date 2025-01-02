# 백준 수 정렬하기 3 문제이다.
# 문제 번호는 10989번

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 10001

for i in range(n):
    arr[int(input())] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
