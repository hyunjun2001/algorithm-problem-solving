# 백준 ATM 문제이다.
# 문제 번호는 11399번
# 아래 풀이는 삽입정렬을 연습하기 위해 일부러 저렇게 풀었고 그냥 sort()로 적용하는 게 더 빠름

import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
ans = 0

for end in range(0, n):
    for i in range(end, 0, -1):
        if arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

for i in range(1, n+1):
    for j in range(0, i):
        ans += arr[j]

print(ans)

