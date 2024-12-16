# 백준 동전 0 문제이다.
# 문제 번호는 11047번

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

arr = []
count = 0

for i in range(n):
    arr.append(int(input().strip()))

for j in range(len(arr)-1, -1, -1):
    temp = k // arr[j]
    count += temp
    k = k - (arr[j] * temp)

print(count)

